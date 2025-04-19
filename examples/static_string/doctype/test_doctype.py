"""Test an example."""

import pytest

from . import main


@pytest.mark.skip("Need implementation of escaping")
def test_main() -> None:
    """Ensure the demo matches expected."""
    assert str(main()) == "<!DOCTYPE html><div>Hello World</div>"
