import json


def json_encode(p):
    # There can be NO SPACES in the json
    return json.dumps(p, separators=(",", ":"))


def add_header(c):
    # CMAN+4 bytes = length of command
    # length of the json string
    header = b"CMAN"  # In all commands
    command = bytes(json_encode(c), encoding="utf-8")  # No spaces allowed
    command_length = len(command)
    length_bytes = command_length.to_bytes(4, "big")  # I wonder if they check bounds?
    return header + length_bytes + command


class command(object):
    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        return add_header(self.f(*args, **kwargs))
