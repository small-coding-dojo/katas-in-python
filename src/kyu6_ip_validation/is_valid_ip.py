from ipaddress import IPv4Address


def is_valid_IP(input):
    try:
        IPv4Address(input)
        return True
    except:
        return False
