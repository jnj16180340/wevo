camera_general_notification = {
    "command": "camera_general_notification",
    "data": {"not_recovered_packets": 0, "stream_health": "Perfect streaming"},
    "description": "Streaming info",
    "id": 0,
}

rtmp_queue_notification = {
    "antilag_count": 0,
    "audio_queue_size": 3,
    "command": "rtmp_queue_notification",
    "thinout_count": 0,
    "video_queue_size": 1,
}

camera_error_notification = {
    "command": "camera_error_notification",
    "error_code": 49,
    "error_description": "RTMP error",
    "http_code": 0,
    "title": "Unable to go live on Custom RTMP",
}

studio_mode_did_change_notification = {
    "command": "studio_mode_did_change_notification",
    "studio_mode": 1,
}

stream_backup_started_notification = (
    {
        "command": "stream_backup_started_notification",
        "stream_backup_file_name": "C:\\DCIM\\100_MEVO\\LIVE0013.MP4",
    },
)
