#!/bin/env python

import ssl
import socket
from functools import reduce
from operator import add

import json

from contextlib import contextmanager

import asyncio
from functools import partial

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

from math import sin, pi


def parse_response(data):
    header = data[:4]
    length = int.from_bytes(data[4:8], "big")
    payload = json.loads(data[8:])
    return header, length, payload


from datetime import datetime


class MevoClientProtocol(asyncio.Protocol):
    def __init__(self, loop, sequence, on_con_lost):
        self.sequence = sequence
        self.loop = loop
        # it seems to close after 20s inactivity
        self.on_con_lost = on_con_lost

    async def pinger(self):
        while True:
            await asyncio.sleep(5)
            log.debug(f"{datetime.now()} ping")
            self.transport.write(ping())

    async def flashy(self):
        theta = 0
        while True:
            await asyncio.sleep(1)
            self.transport.write(set_led_brightness((sin(theta) + 1) * 0.45))
            theta += pi / 6
            log.debug(f"{datetime.now()} LED: {(sin(theta)+1.1)/2}")

    def connection_made(self, transport):
        self.transport = transport
        for item in self.sequence:
            transport.write(item)
            log.debug(f"{datetime.now()} SENT: {item}")
        self.loop.create_task(self.pinger())
        self.loop.create_task(self.flashy())

    def data_received(self, data):
        if data.startswith(b"CMAN"):
            header, length, payload = parse_response(data)
        log.debug(f"{datetime.now()} RECEIVED {header}[{length}]: {payload}")

    def connection_lost(self, exc):
        log.debug("The server closed the connection")
        self.on_con_lost.set_result(True)

    def eof_received(self):
        log.debug(f"{datetime.now()} EOF received - closing")


async def main():
    loop = asyncio.get_running_loop()
    services = await simple_find_service(
        loop=loop, service=MEVO_SERVICES["ls_cameraman"]
    )
    mevo_host = services[0]["server"]  # also 'address', 'address6'
    mevo_port = services[0]["port"]
    log.debug(f"Found Mevo @ {mevo_host}:{mevo_port}")

    sequence = [auth(), ping(), ping(), set_led_brightness(1.0), ping()]

    on_con_lost = loop.create_future()
    protocol = lambda: MevoClientProtocol(loop, sequence, on_con_lost)
    transport, protocol = await loop.create_connection(
        protocol,
        host=mevo_host,
        port=mevo_port,
        ssl=ssl.SSLContext(protocol=ssl.PROTOCOL_TLSv1_2),
    )

    # Wait until the protocol signals that the connection
    # is lost and close the transport.
    try:
        await on_con_lost
    finally:
        transport.close()


if __name__ == "__main__":
    asyncio.run(main())
