#!/bin/env python
"""
A simple example of using Python sockets for a client HTTPS connection.
"""

import ssl
import socket
import json
from functools import reduce
from operator import add

def json_encode(p):
    # There can be NO SPACES in the json
    return json.dumps(p,separators=(',', ':'))

def add_header(c):
    # CMAN+4 bytes = length of command
    # length of the json string
    header = b'CMAN'  # In all commands
    command = bytes(json_encode(c), encoding='utf-8')  # No spaces allowed
    command_length = len(command)
    length_bytes = command_length.to_bytes(4, 'big')  # I wonder if they check bounds?
    return header+length_bytes+command
    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.69.19', 38000))
s = ssl.wrap_socket(s, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE, ssl_version=ssl.PROTOCOL_TLSv1_2)
    
# Look for 'preview_enabled':
# Binary file WinSW/LivestreamStudioMac/PayloadFolder/Payload.uncompressed matches
# Binary file WinSW/LivestreamStudioMac/PayloadFolder/Contents/MacOS/LSStudio matches


command_auth = {
    'app_name': 'studio',
    'app_version': '6.3.0',
    'client_id': '{f244e834-9230-437c-9d02-c4059b44b42b}',
    'client_type': 1,
    'command': 'authorize',
    'password': ''
}

command_ping = {
    "command":"ping"
}

command_start_session = {
    "command":"start_studio_session",
    "ping_interval":5,
    "preview_enabled":False,
    #"session_id":8,    # Not strictly necessary?
    "studio_mode":4,
    "udp_ip":"127.0.0.1",
    "udp_port":60300,
    "zixi_url":"zixi://127.0.0.1:50736/studio",
    "zixi_url_ffov":"zixi://127.0.0.1:51775/studio"
}

# NB: BAD INPUT CAN CRASH IT REQUIRING A REBOOT
command_test = {
    "command":"get_settings",
    "settings":["protocol_version","streaming_interface","firmware_version","serial_number"]
}

command_get_supported_frame_rates = {
    "command": "get_supported_frame_rates"
}

# reboots it...
command_reboot = {
    "command":"reboot"
}

command_stop_session = {"command":"stop_studio_session"}

# http://cdn.livestream.com/mevo/settings.json

# no args I think
command_stream_start = {"command": "stream_start"}

command_stream_stop = {"command": "stream_stop"}

# want to make sure it is not saving to sdcard!
command_stream_config = {
      "command": "stream_config",
      "custom_rtmp": {
        "rtmp_url": "rtmp://192.168.69.10/live",
        "stream_name": "livekey",
        "stream_title": "piff"
      },
      "metadata": {
        "force_save_record": False
      },
      "pgm_height": 720,
      "pgm_width": 1280,
      "qualities": [
        {
          "audio_settings": {
            "bitrate": 48,
            "channels_per_frame": 2,
            "constant_bitrate": False,
            "sample_rate": 48000
          },
          "quality_name": "Mobile",
          "video_settings": {
            "bitrate": 150,
            "constant_bitrate": False,
            "height": 270,
            "keyframe_interval": 1,
            "max_bitrate": 300,
            "min_bitrate": 100,
            "width": 480
          }
        },
        {
          "audio_settings": {
            "bitrate": 96,
            "channels_per_frame": 2,
            "constant_bitrate": False,
            "sample_rate": 48000
          },
          "quality_name": "Normal",
          "video_settings": {
            "bitrate": 350,
            "constant_bitrate": False,
            "height": 288,
            "keyframe_interval": 1,
            "max_bitrate": 500,
            "min_bitrate": 250,
            "width": 512
          }
        },
        {
          "audio_settings": {
            "bitrate": 96,
            "channels_per_frame": 2,
            "constant_bitrate": False,
            "sample_rate": 48000
          },
          "quality_name": "Medium",
          "video_settings": {
            "bitrate": 550,
            "constant_bitrate": False,
            "height": 432,
            "keyframe_interval": 1,
            "max_bitrate": 850,
            "min_bitrate": 450,
            "width": 768
          }
        },
        {
          "audio_settings": {
            "bitrate": 128,
            "channels_per_frame": 2,
            "constant_bitrate": False,
            "sample_rate": 48000
          },
          "quality_name": "High",
          "video_settings": {
            "bitrate": 1500,
            "constant_bitrate": False,
            "height": 480,
            "keyframe_interval": 1,
            "max_bitrate": 2500,
            "min_bitrate": 1000,
            "width": 848
          }
        },
        {
          "audio_settings": {
            "bitrate": 256,
            "channels_per_frame": 2,
            "constant_bitrate": False,
            "sample_rate": 48000
          },
          "quality_name": "HD",
          "video_settings": {
            "bitrate": 2000,
            "constant_bitrate": False,
            "height": 720,
            "keyframe_interval": 1,
            "max_bitrate": 3000,
            "min_bitrate": 1000,
            "width": 1280
          }
        },
        {
          "audio_settings": {
            "bitrate": 256,
            "channels_per_frame": 2,
            "constant_bitrate": False,
            "sample_rate": 48000
          },
          "quality_name": "Full HD",
          "video_settings": {
            "bitrate": 4500,
            "constant_bitrate": False,
            "height": 1080,
            "keyframe_interval": 1,
            "max_bitrate": 6750,
            "min_bitrate": 3500,
            "width": 1920
          }
        }
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
        "thin_drop_duration": 2
      },
      "stream_type": 2
    }

sequence = [
    command_auth,
    command_ping,
    #command_start_session,  # does get_settings work without this?
    command_ping,
    #command_reboot,
    #command_test,
    command_ping,
    command_ping,
    command_stop_session
]

sequence_rtmp = [
    command_auth,
    command_ping,
    command_stream_config,
    command_stream_start,
    command_ping
    ]

sequence_rtmp_stop = [
    command_auth,
    command_ping,
    command_stream_stop,
    command_ping
    ]

sequence = sequence_rtmp_stop

sendme = [add_header(s) for s in sequence]
sendme = reduce(add, sendme)

print('\nSENDING DATA:')
print(sendme)

# SEND THE DATA
s.sendall(sendme)

# WAIT FOR A RESPONSE
print('\nRESPONSE:')
while True:

    new = s.recv(4096)
    if not new:
      s.close()
      break
    print(f'{new}')
    #print(new)
    
