"""Inspect functions and dataclasses to match props to args."""

from dataclasses import is_dataclass, fields
from inspect import signature


def get_param_names(target):
    """Find what is needed from a component target function / dataclass."""
    if is_dataclass(target):
        names = [field.name for field in fields(target)]
    else:
        names = [param.name for param in signature(target).parameters.values()]
    return names


def make_kwargs(component, provided_props, children):
    available_props = provided_props | {"children": children}
    return {
        param: available_props[param]
        for param in get_param_names(component)
        if param in available_props
    }
