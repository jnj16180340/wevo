#!/usr/bin/env python

SERVICE = "_ls-cameraman._tcp.local."
SERVICE_DISCOVERY_TIMEOUT = 5  # s
STOP_AFTER_FIRST = True


import asyncio
import socket

from aiozeroconf import (
    ServiceBrowser,
    ServiceStateChange,
    Zeroconf,
    ZeroconfServiceTypes,
)

import netifaces

import logging
from sys import stderr

logging.basicConfig(
    level=logging.DEBUG, format="%(name)s: %(message)s", stream=stderr,
)
log = logging.getLogger("zeroconf-servicediscovery")


async def on_service_state_change_process(zc, service_type, name, cls):
    info = await zc.get_service_info(service_type, name)
    # print("Service %s of type %s state changed: %s" % (name, service_type, ServiceStateChange.Added))
    info_dict = info.__dict__
    info_dict["address"] = socket.inet_ntoa(info.address)
    info_dict["address6"] = socket.inet_ntop(netifaces.AF_INET6, info.address6)
    info_dict["properties"] = info_dict[
        "_properties"
    ]  # {k.decode():v.decode() for k,v in info.properties.items()}
    # for some reason we can't actually enumerate the properties or it hangs!
    del info_dict["text"]
    del info_dict["_properties"]
    cls.found_services.append(info_dict)
    # print(info_dict)


class ZeroconfServiceTypes(object):
    """
    Return all of the advertised services on any local networks
    """

    def __init__(self):
        self.found_services = list()

    def add_service(self, zc, service_type, name):
        # self.found_services.add(name)
        asyncio.create_task(
            on_service_state_change_process(zc, service_type, name, self)
        )

    def remove_service(self, zc, type_, name):
        pass

    @classmethod
    async def find(cls, zc, service, timeout=5, stop_after_first=STOP_AFTER_FIRST):
        """
        Return all of the advertised services on any local networks.
        :param zc: Zeroconf() instance.  Pass in an instance running
        :param timeout: seconds to wait for any responses
        :return: tuple of service type strings
        """
        listener = cls()
        browser = ServiceBrowser(zc, service, listener=listener)

        # wait for responses
        for i in range(100):
            await asyncio.sleep(timeout / 100)
            if len(listener.found_services) > 0 and STOP_AFTER_FIRST:
                break

        browser.cancel()
        # print(listener.found_services)
        return listener.found_services


async def do_close(zc):
    await zc.close()
    log.debug("Closed zeroconf")


async def simple_find_service(
    loop,
    service=SERVICE,
    timeout=SERVICE_DISCOVERY_TIMEOUT,
    stop_after_first=STOP_AFTER_FIRST,
):
    # result = await z.get_service_info(type_=SERVICE, name=SERVICE, timeout=SERVICE_DISCOVERY_TIMEOUT)
    log.debug("Starting zeroconf discovery")
    zeroconf = Zeroconf(loop)
    result = await ZeroconfServiceTypes.find(
        zeroconf, service=service, timeout=timeout, stop_after_first=stop_after_first
    )
    # print(result)
    await do_close(zeroconf)
    return result


if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        # loop.create_task(entrypoint(loop))
        result = loop.run_until_complete(
            simple_find_service(loop, service=SERVICE, stop_after_first=True)
        )
        log.info(f"Found services: {result}")
    except KeyboardInterrupt:
        print("Unregistering...")
        # loop.run_until_complete(do_close(zeroconf))
        print("Unregister complete")
    finally:
        loop.close()
