#!/usr/bin/env bash

### Connecting to it
_MY_IP=$(hostname -I | awk '{print $1}')
echo "URLs (camera): 'rtmp://${_MY_IP}/mevo0', stream key 'mevo' (Or whatever you set it to!), 1935 is default RTMP port"
echo URLs (VLC): "rtmp://${_MY_IP}/live/livekey"     
echo "URLs (nginx stats): 'http://localhost:8080/stat'"

### NGINX / nginx-rtmp stream server
docker run      \
  -p 1935:1935        \
  -p 8080:8080        \
  -e RTMP_STREAM_NAMES=mevo0,mevo1,mevo2   \
  jasonrivers/nginx-rtmp

