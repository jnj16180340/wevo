#!/bin/env python

import ssl
import socket
from functools import reduce
from operator import add

import json

from contextlib import contextmanager

import asyncio

import logging
from sys import stderr

logging.basicConfig(
    level=logging.DEBUG, format="%(name)s: %(message)s", stream=stderr,
)
log = logging.getLogger("main")

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

async def pinger(writer):
    while True:
        await asyncio.sleep(2)
        writer.write(ping())
        await writer.drain()
        log.debug(f"SENT: {ping()}")


async def poller(reader):
    while True:
        # "CMAN <length> <JSON>"
        data = await reader.read(4)
        # if data:
        #    log.debug(data)
        if data == b"CMAN":
            length = int.from_bytes(await reader.read(4), "big")
            payload = await reader.read(length)
            parsed_payload = json.loads(payload)
            log.info(f"RECEIVED: {parsed_payload}")
        await asyncio.sleep(0.1)
        
async def sender(writer, sequence):
    for sendme in sequence:
        writer.write(sendme)
        await writer.drain()
        log.debug(f"SENT: {sendme}")
        await asyncio.sleep(0.1)


async def main():
    reader, writer = await asyncio.open_connection(
        host=MEVO_HOST,
        port=MEVO_PORT,
        ssl=ssl.SSLContext(protocol=ssl.PROTOCOL_TLSv1_2),
    )
    

    asyncio.create_task(pinger(writer))

    asyncio.create_task(poller(reader))
    
    await sender(writer, sequence)
    await asyncio.sleep(10)

    #while True:
    #    if len(sequence) > 0:
    #        sendme = sequence.pop(0)
    #        writer.write(sendme)
    #        await writer.drain()
    #        log.debug(f"SENT: {sendme}")
    #    await asyncio.sleep(0.25)

if __name__ == "__main__":
    asyncio.run(main())
