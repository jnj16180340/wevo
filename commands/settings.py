from . import command


@command
def get_network_configuration():
    return {"command": "get_network_configuration"}


# TODO set_network_configuration

get_network_configuration_result = (
    {
        "command": "get_network_configuration_result",
        "error_code": 0,
        "error_description": "",
        "ethernet": {
            "dhcp": True,
            "dns": "192.168.69.1",
            "gateway": "192.168.69.1",
            "ip": "192.168.69.19",
            "method_type": 1,
            "subnet_mask": "255.255.255.0",
        },
        "hotspot": {
            "auto_channel": True,
            "channel": 0,
            "frequency": 1,
            "ip": "",
            "password": "",
            "ssid": "Mevo-53898",
        },
        "result": True,
        "wi_fi": {},
    },
)


@command
def set_time(
    unix_time=None, time_zone_gmt_offset_seconds=None, daylight_saving_time=True
):
    # NB: I don't know if this is local or utc timestamp
    return {
        "command": "set_time",
        "daylight_saving_time": daylight_saving_time,
        "time_zone_gmt_offset_seconds": time_zone_gmt_offset_seconds
        if time_zone_gmt_offset_seconds
        else -time.timezone,
        "unix_time": unix_time if unix_time else int(time.time_ns() / 1000),
    }


set_time_result = {
    "command": "set_time_result",
    "error_code": 0,
    "error_description": "",
    "result": True,
}

@command
def set_led_brightness(brightness=1):
    # NB: Setting above 1 kills it...
    return {
        "command": "set_settings",
        #"gfx_demo_mode": false,
        "led_brightness": brightness,
        }

# May not have taken effect yet when this is received, see notification
set_settings_result = {
    "command": "set_settings_result",
    "error_code": 0,
    "error_description": "",
    "result": True,
    "unapplied": [],
}
