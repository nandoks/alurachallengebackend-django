import re

def validate_hexadecimal(color):
    hex_color_regex = "^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"

    response = re.findall(hex_color_regex, color)
    return response

def validate_title(title):
    return len(title) >= 5

