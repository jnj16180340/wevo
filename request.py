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

sequence = [
    command_auth,
    command_ping,
    command_start_session,  # does get_settings work without this?
    command_ping,
    #command_reboot,
    command_test,
    command_ping,
    command_ping,
    command_stop_session
]
#sequence=[command_stop_session]

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
    
