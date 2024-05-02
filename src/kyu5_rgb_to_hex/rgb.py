def rgb(r, g, b):
    return f"{hex_short(r)}{hex_short(g)}{hex_short(b)}"


def hex_short(value):
    value = clamp(value, 0, 255)
    return ("0" + hex(value)[2:])[-2:].upper()


def clamp(value, low, high):
    return max(min(value, high), low)
