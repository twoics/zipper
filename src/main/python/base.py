from fbs_runtime.application_context.PyQt5 import ApplicationContext
from typing import Union
import json

LIGHT_THEME = "light"
DARK_THEME = "dark"

BASE_CONTEXT = ApplicationContext()


def get_color_from_json() -> dict:
    with open(BASE_CONTEXT.get_resource("color_data.json")) as json_file:
        json_dict = json.load(json_file)
        style_type = json_dict['style']
        if style_type == LIGHT_THEME:
            result_dict = json_dict['colors_light']
        else:
            result_dict = json_dict['colors_dark']
    return result_dict


def change_current_color_in_json() -> None:
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
