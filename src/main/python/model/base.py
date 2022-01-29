"""Module containing a link to the Application Context and functions for working with resources"""

# Standard library imports
import json
from typing import Union

# Third party imports
from fbs_runtime.application_context.PyQt5 import ApplicationContext

LIGHT_THEME = "light"
DARK_THEME = "dark"

BASE_CONTEXT = ApplicationContext()


def get_current_colors_from_json() -> dict:
    """
    Return colors for current theme-style
    :return: dict with colors from json
    """
    with open(BASE_CONTEXT.get_resource("color_data.json")) as json_file:
        json_dict = json.load(json_file)
        style_type = json_dict['style']
        if style_type == LIGHT_THEME:
            result_dict = json_dict['colors_light']
        else:
            result_dict = json_dict['colors_dark']
    return result_dict


def change_current_theme_in_json() -> None:
    """
    Changes the current theme to another: dark to light and vice versa
    :return: None
    """
    # Replace color-style in json
    with open(BASE_CONTEXT.get_resource("color_data.json")) as json_file:
        data = json.load(json_file)

        # If the current color is light, set to dark, and vice versa
        data["style"] = DARK_THEME if data["style"] == LIGHT_THEME else LIGHT_THEME

    with open(BASE_CONTEXT.get_resource("color_data.json"), "w") as json_file:
        json.dump(data, json_file)


def get_current_theme_style() -> Union[LIGHT_THEME, DARK_THEME]:
    with open(BASE_CONTEXT.get_resource("color_data.json")) as json_file:
        style = json.load(json_file)["style"]
    return style
