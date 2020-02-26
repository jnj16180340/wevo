from . import command


@command
def start_remote_audio_session():
    # Configured in Settings?
    return {"command": "start_remote_audio_session"}


start_remote_audio_session_result = {
    "command": "start_remote_audio_session_result",
    "error_code": 0,
    "error_description": "",
    "port_audio": 33781,
    "port_sync": 55415,
    "result": True,
    "session_id": 2,
    "ticks_per_sample": 20,
    "ticks_per_second": 960000,
}
