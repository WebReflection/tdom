import pytest

from tdom import html


def test_preserve_newlines():
    """Don't strip out newlines"""
    result = html(t"<!DOCTYPE html>\n<body>\n<div>Hello World</div>\n</body>")
    assert str(result) == "<!DOCTYPE html><body><div>Hello World</div></body>"


def test_position_args_components():
    """Passing props and children for direct components vs. indirect."""

    def OtherHeading():
        """Another heading used in another condition."""
        return html(t"<h1>Other Heading</h1>")

    def Body(props, children):
        """Render the body with a heading based on which is passed in."""
        heading = props.get("heading")
        return html(t"<body>{heading if heading else DefaultHeading}</body>")

    # If OtherHeading is called directly, it fails, needs props and children
    with pytest.raises(TypeError) as excinfo:
        html(t"<{OtherHeading} />")
    assert str(excinfo.value).endswith("but 2 were given")

    # But if it is passed in an attribute value, it does NOT need props/children
    # in the function signature.
    result = html(t"<{Body} heading={OtherHeading}/>")
    assert str(result) == "<body><h1>Other Heading</h1></body>"
