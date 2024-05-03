import re


def is_valid_IP(input):
    print(f"'{input}'")
    if input != input.strip():
        return False

    match = re.match("^(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})$", input)

    if not match:
        return False

    groups = match.groups()
    for number_string in groups:
        number = int(number_string)
        if number_string != str(number) or number < 0 or number > 255:
            return False

    return True
