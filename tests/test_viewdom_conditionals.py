"""
Port the code from viewdom.examples.conditionals.
"""

import pytest

from tdom import html


def test_syntax():
    """Use normal Python syntax for conditional rendering in a template."""
    message = "Say Howdy"
    not_message = "So Sad"
    show_message = True
    result = html(
        t"""
        <h1>Show?</h1>
        {message if show_message else not_message}
    """
    )
    assert str(result) == "<h1>Show?</h1>Say Howdy"
