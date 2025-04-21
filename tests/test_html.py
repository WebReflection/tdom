"""Components can be any kind of dataclass_component."""

from dataclasses import dataclass

import pytest

from tdom import _util
from tdom.component_signature import make_kwargs
from tdom.dom import _replaceWith


def _injector_builder(node, component, props, children, context):
    """A different builder that passes in props by name."""
    kwargs = make_kwargs(component, props, children)
    # Is this a function or a class/dataclass?
    if component.__class__.__name__ == "function":
        value_ = component(**kwargs)
    else:
        # Construct an instance, then call it
        instance_ = component(**kwargs)
        value_ = instance_()
    return _replaceWith(node, value_)


@pytest.fixture
def injector_html():
    """Make a new template function with a different builder policy."""

    return _util(False, context={"builder": _injector_builder})


def test_dataclass(injector_html):
    """Component as a dataclass."""

    @dataclass
    class Greeting:
        """Give a greeting."""

        name: str

        def __call__(self):
            """Render to a string."""
            return injector_html(t"Hello {self.name}")

    result = injector_html(t'<div><{Greeting} name="World" /></div>')
    assert str(result) == "<div>Hello World</div>"


def test_dataclass_extra_arg(injector_html):
    """The caller passes in an argument the component wasn't expecting."""

    @dataclass
    class Greeting:
        """Give a greeting."""

        name: str

        def __call__(self):
            """Render to a string."""
            return injector_html(t"Hello {self.name}")

    result = injector_html(t'<div><{Greeting} name="World" /></div>')
    assert str(result) == "<div>Hello World</div>"


def test_function(injector_html):
    """Component as a function."""

    def Greeting(name):
        return injector_html(t"Hello {name}")

    result = injector_html(t'<div><{Greeting} name="World" /></div>')
    assert str(result) == "<div>Hello World</div>"


def test_function_children(injector_html):
    """Component also asks for children."""

    def Greeting(name, children):
        return injector_html(t"Hello {name}")

    result = injector_html(t'<div><{Greeting} name="World" /></div>')
    assert str(result) == "<div>Hello World</div>"


def test_function_extra_arg(injector_html):
    """The caller passes in an argument the component wasn't expecting."""

    def Greeting(name):
        return injector_html(t"Hello {name}")

    result = injector_html(t'<div><{Greeting} name="World" extra="barf" /></div>')
    assert str(result) == "<div>Hello World</div>"
