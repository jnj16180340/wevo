### Connecting to it
URLs (camera):`rtmp://192.168.69.10/live`, stream key `livekey`, 1935 is default RTMP port  
URLs (VLC): `rtmp://192.168.69.10/live/livekey`     
URLs (nginx stats): `http://localhost:8080/stat`     

### NGINX / nginx-rtmp stream server

```
docker run      \
  -p 1935:1935        \
  -p 8080:8080        \
  -e RTMP_STREAM_NAMES=live,teststream1,teststream2   \
  jasonrivers/nginx-rtmp
```
