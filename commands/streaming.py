from . import command


@command
def get_supported_frame_rates():
    return {"command": "get_supported_frame_rates"}


get_supported_frame_rates_result = {
    "command": "get_supported_frame_rates_result",
    "error_code": 0,
    "error_description": "",
    "result": True,
    "supported_frame_rates": [
        {"time_scale": 30000, "value": 1001},
        {"time_scale": 25, "value": 1},
        {"time_scale": 30000, "value": 1000},
        {"time_scale": 50, "value": 1},
        {"time_scale": 60000, "value": 1001},
        {"time_scale": 60000, "value": 1000},
    ],
}

# want to make sure it is not saving to sdcard!
# http://cdn.livestream.com/mevo/settings.json
# TODO
@command
def stream_config(
    endpoint="192.168.69.10/live", stream_name="livekey", stream_title="piff"
):
    # RTMP only - see stream_type
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


stream_config_result = {
    "command": "stream_config_result",
    "error_code": 0,
    "error_description": "",
    "result": True,
}


@command
def stream_stop():
    return {"command": "stream_stop"}


@command
def stream_start():
    return {"command": "stream_start"}


stream_start_result = {
    "command": "stream_start_result",
    "error_code": 0,
    "error_description": "",
    "result": True,
}


@command
def stop_ffov_stream():
    return {"command": "stop_ffov_stream"}


stop_ffov_stream_result = {
    "command": "stop_ffov_stream_result",
    "error_code": 0,
    "error_description": "",
    "result": True,
}


@command
def start_ffov_stream():
    return {"command": "start_ffov_stream"}


start_ffov_stream_result = {
    "command": "start_ffov_stream_result",
    "error_code": 0,
    "error_description": "",
    "result": True,
}

# TODO
@command
def start():
    # This seems to be for Zixi protocol stream only
    return {
        "bitrate_control_config": {
            "ffov": {
                "960x540x30": {
                    "adaptive_streaming": false,
                    "audio_bitrate_kbps": 128,
                    "backup_stream": false,
                    "fps": 30,
                    "video_bitrate_max_kbps": 1250,
                    "video_bitrate_min_kbps": 1250,
                    "video_height": 540,
                    "video_width": 960,
                }
            },
            "lte_streaming": {
                "1056x1056x30": {
                    "adaptive_streaming": True,
                    "audio_bitrate_kbps": 128,
                    "backup_stream": True,
                    "fps": 30,
                    "video_bitrate_max_kbps": 4000,
                    "video_bitrate_min_kbps": 1200,
                    "video_height": 1056,
                    "video_width": 1056,
                },
                "1280x720x30": {
                    "adaptive_streaming": True,
                    "audio_bitrate_kbps": 128,
                    "backup_stream": True,
                    "fps": 30,
                    "video_bitrate_max_kbps": 2000,
                    "video_bitrate_min_kbps": 700,
                    "video_height": 720,
                    "video_width": 1280,
                },
                "1920x1080x30": {
                    "adaptive_streaming": True,
                    "audio_bitrate_kbps": 128,
                    "backup_stream": True,
                    "fps": 30,
                    "video_bitrate_max_kbps": 6000,
                    "video_bitrate_min_kbps": 1200,
                    "video_height": 1080,
                    "video_width": 1920,
                },
                "384x384x30": {
                    "adaptive_streaming": True,
                    "audio_bitrate_kbps": 64,
                    "backup_stream": True,
                    "fps": 30,
                    "video_bitrate_max_kbps": 1000,
                    "video_bitrate_min_kbps": 300,
                    "video_height": 384,
                    "video_width": 384,
                },
                "480x480x30": {
                    "adaptive_streaming": True,
                    "audio_bitrate_kbps": 96,
                    "backup_stream": True,
                    "fps": 30,
                    "video_bitrate_max_kbps": 1500,
                    "video_bitrate_min_kbps": 400,
                    "video_height": 480,
                    "video_width": 480,
                },
                "640x360x30": {
                    "adaptive_streaming": True,
                    "audio_bitrate_kbps": 64,
                    "backup_stream": True,
                    "fps": 30,
                    "video_bitrate_max_kbps": 1000,
                    "video_bitrate_min_kbps": 300,
                    "video_height": 360,
                    "video_width": 640,
                },
                "736x736x30": {
                    "adaptive_streaming": True,
                    "audio_bitrate_kbps": 128,
                    "backup_stream": True,
                    "fps": 30,
                    "video_bitrate_max_kbps": 2000,
                    "video_bitrate_min_kbps": 700,
                    "video_height": 736,
                    "video_width": 736,
                },
                "864x480x30": {
                    "adaptive_streaming": True,
                    "audio_bitrate_kbps": 96,
                    "backup_stream": True,
                    "fps": 30,
                    "video_bitrate_max_kbps": 1500,
                    "video_bitrate_min_kbps": 400,
                    "video_height": 480,
                    "video_width": 864,
                },
                "960x540x30": {
                    "adaptive_streaming": True,
                    "audio_bitrate_kbps": 96,
                    "backup_stream": True,
                    "fps": 30,
                    "video_bitrate_max_kbps": 800,
                    "video_bitrate_min_kbps": 400,
                    "video_height": 540,
                    "video_width": 960,
                },
            },
            "sd_recording": {
                "1280x720x30": {
                    "adaptive_streaming": false,
                    "audio_bitrate_kbps": 128,
                    "backup_stream": false,
                    "fps": 30,
                    "video_bitrate_max_kbps": 10000,
                    "video_bitrate_min_kbps": 10000,
                    "video_height": 720,
                    "video_width": 1280,
                },
                "1920x1080x30": {
                    "adaptive_streaming": false,
                    "audio_bitrate_kbps": 128,
                    "backup_stream": false,
                    "fps": 30,
                    "video_bitrate_max_kbps": 20000,
                    "video_bitrate_min_kbps": 20000,
                    "video_height": 1080,
                    "video_width": 1920,
                },
                "3840x2160x30": {
                    "adaptive_streaming": false,
                    "audio_bitrate_kbps": 128,
                    "backup_stream": false,
                    "fps": 30,
                    "video_bitrate_max_kbps": 40000,
                    "video_bitrate_min_kbps": 40000,
                    "video_height": 2160,
                    "video_width": 3840,
                },
            },
            "studio_mode": {
                "1280x720x30": {
                    "adaptive_streaming": True,
                    "audio_bitrate_kbps": 128,
                    "backup_stream": false,
                    "fps": 30,
                    "video_bitrate_max_kbps": 7500,
                    "video_bitrate_min_kbps": 2500,
                    "video_height": 720,
                    "video_width": 1280,
                },
                "1280x720x30x5000": {
                    "adaptive_streaming": True,
                    "audio_bitrate_kbps": 128,
                    "backup_stream": false,
                    "fps": 30,
                    "video_bitrate_max_kbps": 5000,
                    "video_bitrate_min_kbps": 2500,
                    "video_height": 720,
                    "video_width": 1280,
                },
                "1920x1080x30": {
                    "adaptive_streaming": True,
                    "audio_bitrate_kbps": 128,
                    "backup_stream": false,
                    "fps": 30,
                    "video_bitrate_max_kbps": 15000,
                    "video_bitrate_min_kbps": 10000,
                    "video_height": 1080,
                    "video_width": 1920,
                },
            },
            "wifi_streaming": {
                "1056x1056x30": {
                    "adaptive_streaming": True,
                    "audio_bitrate_kbps": 128,
                    "backup_stream": True,
                    "fps": 30,
                    "video_bitrate_max_kbps": 4000,
                    "video_bitrate_min_kbps": 1200,
                    "video_height": 1056,
                    "video_width": 1056,
                },
                "1280x720x30": {
                    "adaptive_streaming": True,
                    "audio_bitrate_kbps": 128,
                    "backup_stream": True,
                    "fps": 30,
                    "video_bitrate_max_kbps": 3500,
                    "video_bitrate_min_kbps": 700,
                    "video_height": 720,
                    "video_width": 1280,
                },
                "1920x1080x30": {
                    "adaptive_streaming": True,
                    "audio_bitrate_kbps": 128,
                    "backup_stream": True,
                    "fps": 30,
                    "video_bitrate_max_kbps": 6000,
                    "video_bitrate_min_kbps": 1200,
                    "video_height": 1080,
                    "video_width": 1920,
                },
                "384x384x30": {
                    "adaptive_streaming": True,
                    "audio_bitrate_kbps": 64,
                    "backup_stream": True,
                    "fps": 30,
                    "video_bitrate_max_kbps": 1000,
                    "video_bitrate_min_kbps": 300,
                    "video_height": 384,
                    "video_width": 384,
                },
                "480x480x30": {
                    "adaptive_streaming": True,
                    "audio_bitrate_kbps": 96,
                    "backup_stream": True,
                    "fps": 30,
                    "video_bitrate_max_kbps": 1500,
                    "video_bitrate_min_kbps": 400,
                    "video_height": 480,
                    "video_width": 480,
                },
                "640x360x30": {
                    "adaptive_streaming": True,
                    "audio_bitrate_kbps": 64,
                    "backup_stream": True,
                    "fps": 30,
                    "video_bitrate_max_kbps": 1000,
                    "video_bitrate_min_kbps": 300,
                    "video_height": 360,
                    "video_width": 640,
                },
                "736x736x30": {
                    "adaptive_streaming": True,
                    "audio_bitrate_kbps": 128,
                    "backup_stream": True,
                    "fps": 30,
                    "video_bitrate_max_kbps": 2000,
                    "video_bitrate_min_kbps": 700,
                    "video_height": 736,
                    "video_width": 736,
                },
                "864x480x30": {
                    "adaptive_streaming": True,
                    "audio_bitrate_kbps": 96,
                    "backup_stream": True,
                    "fps": 30,
                    "video_bitrate_max_kbps": 1500,
                    "video_bitrate_min_kbps": 400,
                    "video_height": 480,
                    "video_width": 864,
                },
                "960x540x30": {
                    "adaptive_streaming": True,
                    "audio_bitrate_kbps": 96,
                    "backup_stream": True,
                    "fps": 30,
                    "video_bitrate_max_kbps": 800,
                    "video_bitrate_min_kbps": 400,
                    "video_height": 540,
                    "video_width": 960,
                },
            },
        },
        "command": "start",
        "ffov_net_protocol_type": 0,
        "ping_interval": 10,
        "zixi_full_FOV_URL": "zixi://192.168.69.5:43363/full",
        "zixi_stream_config": [
            {
                "aggressiveness": 20,
                "content_aware_fec": 0,
                "enforce_bitrate": 0,
                "fec_block_ms": 100,
                "fec_overhead": 30,
                "force_padding": True,
                "latency_mode": 0,
                "limited": 1,
                "max_latency_ms": 800,
                "name": "PGM from Camera to Cloud",
                "smoothing_latency": 0,
                "update_interval": 0,
                "use_compression": 0,
            },
            {
                "aggressiveness": 0,
                "content_aware_fec": 0,
                "enforce_bitrate": 0,
                "fec_block_ms": 30,
                "fec_overhead": 0,
                "force_padding": false,
                "latency_mode": 0,
                "limited": 0,
                "max_latency_ms": 100,
                "name": "Audio from iOS to Camera",
                "smoothing_latency": 0,
                "update_interval": 0,
                "use_compression": 0,
            },
            {
                "aggressiveness": 50,
                "content_aware_fec": 0,
                "enforce_bitrate": 0,
                "fec_block_ms": 90,
                "fec_overhead": 30,
                "force_padding": false,
                "latency_mode": 1,
                "limited": 1,
                "max_latency_ms": 250,
                "name": "PGM from Camera to Studio",
                "smoothing_latency": 0,
                "update_interval": 0,
                "use_compression": 0,
            },
            {
                "aggressiveness": 0,
                "content_aware_fec": 0,
                "enforce_bitrate": 0,
                "fec_block_ms": 150,
                "fec_overhead": 30,
                "force_padding": false,
                "latency_mode": 0,
                "limited": 1,
                "max_latency_ms": 200,
                "name": "FFOV from Camera",
                "smoothing_latency": 0,
                "update_interval": 0,
                "use_compression": 0,
            },
            {
                "aggressiveness": 20,
                "content_aware_fec": 0,
                "enforce_bitrate": 0,
                "fec_block_ms": 100,
                "fec_overhead": 30,
                "force_padding": True,
                "latency_mode": 2,
                "limited": 1,
                "max_latency_ms": 1000,
                "name": "PGM from iOS to Cloud",
                "smoothing_latency": 0,
                "update_interval": 0,
                "use_compression": 0,
            },
            {
                "aggressiveness": 0,
                "content_aware_fec": 0,
                "enforce_bitrate": 0,
                "fec_block_ms": 150,
                "fec_overhead": 30,
                "force_padding": false,
                "latency_mode": 0,
                "limited": 1,
                "max_latency_ms": 200,
                "name": "PGM from Camera to iOS",
                "smoothing_latency": 0,
                "update_interval": 0,
                "use_compression": 0,
            },
        ],
    }


start_result = {
    "command": "start_result",
    "error_code": 0,
    "error_description": "",
    "ffov_net_protocol_type": 0,
    "result": True,
    "start_timestamp": 0,
}
