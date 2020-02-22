#!/bin/env python
"""
A simple example of using Python sockets for a client HTTPS connection.
"""

import ssl
import socket
from functools import reduce
from operator import add

from contextlib import contextmanager

import asyncio

import logging
from sys import stderr
logging.basicConfig(
    level=logging.DEBUG,
    format='%(name)s: %(message)s',
    stream=stderr,
)
log = logging.getLogger('main')

from commands import (
    auth,
    ping,
    reboot,
    start_studio_session,
    stop_studio_session,
    stream_config,
    stream_start,
    stream_stop,
)

# NB: Should use Bonjour / Avahi / Zeroconf to get this
MEVO_HOST = "192.168.69.19"
MEVO_PORT = 38000


@contextmanager
def mevo_connection(MEVO_IP="192.168.69.19", MEVO_PORT=38000):
    sock = ssl.wrap_socket(
        socket.socket(socket.AF_INET, socket.SOCK_STREAM),
        keyfile=None,
        certfile=None,
        server_side=False,
        cert_reqs=ssl.CERT_NONE,
        ssl_version=ssl.PROTOCOL_TLSv1_2,
    )
    sock.connect((MEVO_IP, MEVO_PORT))
    try:
        yield sock
    finally:
        print('Cleaning up socket...', end='')
        sock.close()
        print('Done')


sequence = [
    auth(),
    ping(),
    # start_session,  # does get_settings work without this?
    ping(),
    # reboot,
    # test,
    # ping,
    # ping,
    # stop_session,
]

# sequence_rtmp = [auth, ping, stream_config, stream_start, ping]
# sequence_rtmp_stop = [auth, ping, stream_stop, ping]
# sequence = sequence_rtmp_stop

async def main():
    reader, writer = await asyncio.open_connection(
        host=MEVO_HOST,
        port=MEVO_PORT,
        ssl=ssl.SSLContext(protocol=ssl.PROTOCOL_TLSv1_2)
    )
    while True: # can we replace w run_until_complete
        #log.info('Waiting for data')
        if len(sequence)>0:
            sendme = sequence.pop(0)
            log.info(f'Sent: {sendme}')
            writer.write(sendme)
            await writer.drain()
        
        data = await reader.readline()
        if data:
            log.info(f'Received: {data}')
        await asyncio.sleep(0.25)

def maine():
    sendme = reduce(add, sequence)

    print("\nSENDING DATA:")
    print(sendme)

    with mevo_connection(MEVO_HOST, MEVO_PORT) as s:
        # SEND THE DATA
        s.sendall(sendme)

        # WAIT FOR A RESPONSE
        print("\nRESPONSE:")
        while True:
            new = s.recv(4096)
            if not new:
                break
            print(f"{new}")
            # print(new)

if __name__ == '__main__':
    asyncio.run(main())
    #maine()


