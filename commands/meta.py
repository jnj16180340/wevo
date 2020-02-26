from . import command


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
        # "app_name": "mevo(android;28;motorola;moto g(7) power)",
        # "app_version": "1.16.8",
        # "client_id": "4544afdc-b68e-39a2-9c8e-f7712db32c88",
    }


@command
def ping():
    return {"command": "ping"}


authorize_result = {
    "command": "authorize_result",
    "error_code": 0,
    "error_description": "",
    "protocol_version": 47,
    "result": True,
    "studio_protocol_version": 1,
}


@command
def reboot():
    # It takes like a full minute to reboot
    return {"command": "reboot"}


@command
def start_studio_session():
    # Seems to be unnecessary
    return {
        "command": "start_studio_session",
        "ping_interval": 5,  # Heartbeat???
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
