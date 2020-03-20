# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Spinner(Component):
    """A Spinner component.


Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The children of this component.
- id (string; optional): The ID of this component, used to identify dash components
in callbacks. The ID needs to be unique across all of the
components in an app.
- style (dict; optional): Defines CSS styles which will override styles previously set.
- spinner_style (dict; optional): Inline CSS styles to apply to the spinner.
- className (string; optional): Often used with CSS to style elements with common properties.
- spinnerClassName (string; optional): CSS class names to apply to the spinner.
- color (string; optional): Spinner color, options: primary, secondary, success, info, warning, danger,
link. If not specified will default to text colour.
- type (string; optional): The type of spinner. Options 'border' and 'grow'. Default 'border'.
- size (string; optional): The spinner size. Options are 'sm', 'md' and 'lg'.
- fullscreen (boolean; optional): Boolean that determines if the loading spinner will be displayed
full-screen or not."""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, style=Component.UNDEFINED, spinner_style=Component.UNDEFINED, className=Component.UNDEFINED, spinnerClassName=Component.UNDEFINED, color=Component.UNDEFINED, type=Component.UNDEFINED, size=Component.UNDEFINED, fullscreen=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'style', 'spinner_style', 'className', 'spinnerClassName', 'color', 'type', 'size', 'fullscreen']
        self._type = 'Spinner'
        self._namespace = 'dash_bootstrap_components/_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'style', 'spinner_style', 'className', 'spinnerClassName', 'color', 'type', 'size', 'fullscreen']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Spinner, self).__init__(children=children, **args)
