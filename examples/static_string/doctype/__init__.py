"""Getting a doctype into the rendered output is a bit tricky."""
from tdom import html


def main():
    """Main entry point."""
    # TODO Andrea Provide something in `__all__` (or add MarkupSafe
    #  as a dependency to make this work correctly)
    doctype = "<!DOCTYPE html>"
    result = html(t"{doctype}<div>Hello World</div>")
    return result
