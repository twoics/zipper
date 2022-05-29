# Standard library imports
import json

# Third party imports
from src.main.python.base import BASE_CONTEXT

LIGHT_THEME = "light"
DARK_THEME = "dark"

CURRENT_STYLE = "current_style"

STYLES = {LIGHT_THEME, DARK_THEME}

LINK_TO_JSON = "color_data.json"


class JsonConnector:
    """
    A class that implements the logic
    for accessing and retrieving values from json
    """

    def __init__(self):
        self._base_context = BASE_CONTEXT

    def get_colors(self, style: str) -> dict:
        """
        The method of obtaining colors, by style: {dark, light}
        :param style: One of {dark, light}
        :return: Dict with colors
        """
        if style not in STYLES:
            raise ValueError(f"Style must be one of {STYLES}")

        with open(self._base_context.get_resource(LINK_TO_JSON)) as json_file:
            json_dict = json.load(json_file)
            if style == LIGHT_THEME:
                return json_dict['colors_light']
            return json_dict['colors_dark']

    def set_current_style(self, style: str) -> None:
        """
        Sets the passed style as the current in JSON
        :param style: One of {dark, light}
        :return: None
        """
        if style not in STYLES:
            raise ValueError(f"Style must be one of {STYLES}")

        # Update value
        with open(self._base_context.get_resource(LINK_TO_JSON)) as json_file:
            data = json.load(json_file)
            data[CURRENT_STYLE] = style

        # Set new value to JSON
        with open(self._base_context.get_resource(LINK_TO_JSON), "w") as json_file:
            json.dump(data, json_file)

    def get_current_style(self) -> str:
        """
        Getting the current style from JSON
        :return: one of {dark, light}
        """
        with open(self._base_context.get_resource(LINK_TO_JSON)) as json_file:
            data = json.load(json_file)
            return data[CURRENT_STYLE]
