"""
The module implements the getting and setting of data in the database
"""

# Standard library imports
import json


class JsonConnector:
    """
    A class that implements the logic
    for accessing and retrieving values from json
    """

    LIGHT_THEME = "light"
    DARK_THEME = "dark"
    STYLES = {LIGHT_THEME, DARK_THEME}

    CURRENT_STYLE_FIELD = "current_style"
    LINK_TO_JSON = "color_data.json"

    def __init__(self, base_context):
        """
        Database communication class
        :param base_context: Application context, to access the db
        """
        self._base_context = base_context

    def get_colors(self, style: str) -> dict:
        """
        The method of getting colors, by style: {dark, light}
        :param style: One of {dark, light}
        :return: Dict with colors
        """
        if style not in self.STYLES:
            raise ValueError(f"Style must be one of {self.STYLES}")

        with open(self._base_context.get_resource(self.LINK_TO_JSON)) as json_file:
            json_dict = json.load(json_file)
            if style == self.LIGHT_THEME:
                return json_dict['colors_light']
            return json_dict['colors_dark']

    def set_current_style(self, style: str) -> None:
        """
        Sets the passed style as the current in JSON
        :param style: One of {dark, light}
        :return: None
        """
        if style not in self.STYLES:
            raise ValueError(f"Style must be one of {self.STYLES}")

        # Update value
        with open(self._base_context.get_resource(self.LINK_TO_JSON)) as json_file:
            data = json.load(json_file)
            data[self.CURRENT_STYLE_FIELD] = style

        # Set new value to JSON
        with open(self._base_context.get_resource(self.LINK_TO_JSON), "w") as json_file:
            json.dump(data, json_file)

    def get_current_style(self) -> str:
        """
        Getting the current style from JSON
        :return: one of {dark, light}
        """
        with open(self._base_context.get_resource(self.LINK_TO_JSON)) as json_file:
            data = json.load(json_file)
            return data[self.CURRENT_STYLE_FIELD]
