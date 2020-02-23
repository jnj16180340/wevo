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


@command
def auth():
    return {
        "app_name": "studio",
        "app_version": "6.3.0",
        #'client_id': '{f244e834-9230-437c-9d02-c4059b44b42b}',
        "client_id": "{beefbeef-beef-beef-beef-beefbeefbeef}",
        "client_type": 1,
        "command": "authorize",
        "password": "",
    }


@command
def ping():
    return {"command": "ping"}


@command
def start_studio_session():
    return {
        "command": "start_studio_session",
        "ping_interval": 5,
        "preview_enabled": False,
        # "session_id":8,    # Not strictly necessary?
        "studio_mode": 4,
        "udp_ip": "127.0.0.1",
        "udp_port": 60300,
        "zixi_url": "zixi://127.0.0.1:50736/studio",
        "zixi_url_ffov": "zixi://127.0.0.1:51775/studio",
    }


@command
def stop_studio_session():
    return {"command": "stop_studio_session"}


@command
def get_supported_frame_rates():
    return {"command": "get_supported_frame_rates"}


@command
def reboot():
    return {"command": "reboot"}


@command
def stream_start():
    return {"command": "stream_start"}


@command
def stream_stop():
    return {"command": "stream_stop"}


# want to make sure it is not saving to sdcard!
# http://cdn.livestream.com/mevo/settings.json
@command
def stream_config(
    endpoint="192.168.69.10/live", stream_name="livekey", stream_title="piff"
):
    return {
        "command": "stream_config",
        "custom_rtmp": {
            "rtmp_url": f"rtmp://{endpoint}",
            "stream_name": f"{stream_name}",
            "stream_title": f"{stream_title}",
        },
        "metadata": {"force_save_record": False},
        "pgm_height": 720,
        "pgm_width": 1280,
        "qualities": [
            {
                "audio_settings": {
                    "bitrate": 48,
                    "channels_per_frame": 2,
                    "constant_bitrate": False,
                    "sample_rate": 48000,
                },
                "quality_name": "Mobile",
                "video_settings": {
                    "bitrate": 150,
                    "constant_bitrate": False,
                    "height": 270,
                    "keyframe_interval": 1,
                    "max_bitrate": 300,
                    "min_bitrate": 100,
                    "width": 480,
                },
            },
            {
                "audio_settings": {
                    "bitrate": 96,
                    "channels_per_frame": 2,
                    "constant_bitrate": False,
                    "sample_rate": 48000,
                },
                "quality_name": "Normal",
                "video_settings": {
                    "bitrate": 350,
                    "constant_bitrate": False,
                    "height": 288,
                    "keyframe_interval": 1,
                    "max_bitrate": 500,
                    "min_bitrate": 250,
                    "width": 512,
                },
            },
            {
                "audio_settings": {
                    "bitrate": 96,
                    "channels_per_frame": 2,
                    "constant_bitrate": False,
                    "sample_rate": 48000,
                },
                "quality_name": "Medium",
                "video_settings": {
                    "bitrate": 550,
                    "constant_bitrate": False,
                    "height": 432,
                    "keyframe_interval": 1,
                    "max_bitrate": 850,
                    "min_bitrate": 450,
                    "width": 768,
                },
            },
            {
                "audio_settings": {
                    "bitrate": 128,
                    "channels_per_frame": 2,
                    "constant_bitrate": False,
                    "sample_rate": 48000,
                },
                "quality_name": "High",
                "video_settings": {
                    "bitrate": 1500,
                    "constant_bitrate": False,
                    "height": 480,
                    "keyframe_interval": 1,
                    "max_bitrate": 2500,
                    "min_bitrate": 1000,
                    "width": 848,
                },
            },
            {
                "audio_settings": {
                    "bitrate": 256,
                    "channels_per_frame": 2,
                    "constant_bitrate": False,
                    "sample_rate": 48000,
                },
                "quality_name": "HD",
                "video_settings": {
                    "bitrate": 2000,
                    "constant_bitrate": False,
                    "height": 720,
                    "keyframe_interval": 1,
                    "max_bitrate": 3000,
                    "min_bitrate": 1000,
                    "width": 1280,
                },
            },
            {
                "audio_settings": {
                    "bitrate": 256,
                    "channels_per_frame": 2,
                    "constant_bitrate": False,
                    "sample_rate": 48000,
                },
                "quality_name": "Full HD",
                "video_settings": {
                    "bitrate": 4500,
                    "constant_bitrate": False,
                    "height": 1080,
                    "keyframe_interval": 1,
                    "max_bitrate": 6750,
                    "min_bitrate": 3500,
                    "width": 1920,
                },
            },
        ],
        "rtmp_settings": {
            "adaptive_bitrate_avg": 3,
            "adaptive_bitrate_decrease": 4,
            "adaptive_bitrate_drop_down": 0.95,
            "adaptive_bitrate_increase": 2,
            "adaptive_bitrate_measure": 5,
            "adaptive_bitrate_send_lag": 1,
            "adaptive_bitrate_send_latency": 0.5,
            "antilag_drop_rest": 500,
            "antilag_max_buffer": 5000,
            "give_up_time": 180000,
            "reconnect_delay": 10000,
            "save_logs": False,
            "thin_drop_count": 3,
            "thin_drop_duration": 2,
        },
        "stream_type": 2,
    }
