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

from bjdisco import simple_find_service

from commands.meta import (
    auth,
    ping,
    reboot,
    start_studio_session,
    stop_studio_session,
)

from commands.streaming import (
    stream_config,
    stream_start,
    stream_stop,
)

from commands.settings import set_led_brightness

MEVO_SERVICES = {
    "ls_cameraman": "_ls-cameraman._tcp.local.",
    "mevo_studio": "_mevo-studio._tcp.local.",
    "sftp_ssh": "_sftp-ssh._tcp.local.",
    "ssh": "_ssh._tcp.local.",
}


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

from math import sin, pi
async def flashy(writer):
    theta = 0
    while True:
        await asyncio.sleep(0.75)
        writer.write(set_led_brightness((sin(theta)+1)/2))
        await writer.drain()
        theta += (pi/6)
        log.debug(f"LED: {(sin(theta)+1)/2}")

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
    for item in sequence:
        writer.write(item)
        await writer.drain()
        log.debug(f"SENT: {item}")
        await asyncio.sleep(0.1)


async def main():
    services = await simple_find_service(
        loop=asyncio.get_event_loop(), service=MEVO_SERVICES["ls_cameraman"]
    )
    mevo_host = services[0]["server"]  # also 'address', 'address6'
    mevo_port = services[0]["port"]
    log.debug(f"Found Mevo @ {mevo_host}:{mevo_port}")

    reader, writer = await asyncio.open_connection(
        host=mevo_host,
        port=mevo_port,
        ssl=ssl.SSLContext(protocol=ssl.PROTOCOL_TLSv1_2),
    )

    asyncio.create_task(pinger(writer))

    asyncio.create_task(poller(reader))
    
    asyncio.create_task(flashy(writer))

    await sender(writer, sequence)
    await asyncio.sleep(10)


if __name__ == "__main__":
    asyncio.run(main())
