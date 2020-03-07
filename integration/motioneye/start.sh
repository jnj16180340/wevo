#!/usr/bin/env bash

# ccrisan/motioneye:0.42-amd64

docker run --name="motioneye" \
    -p 8765:8765 \
    -p 8081:8081 \
    -p 8082:8082 \
    -p 8083:8083 \
    --hostname="motioneye" \
    -v /etc/localtime:/etc/localtime:ro \
    -v /home/nate/Projects/wevo/integration/motioneye/etc/motioneye:/etc/motioneye \
    -v /home/nate/Projects/wevo/integration/motioneye/var/lib/motioneye:/var/lib/motioneye \
    --restart="always" \
    --detach=true \
    ccrisan/motioneye:master-amd64

