### Stuff that is less effective
- MITMProxy, CharlesProxy: You can capture some traffic, but it seems some apps do cert pinning... need to work around that
- Decompiling the macos/windows app... it's big
- firmware update payload: very interesting

### MevoResearchLogger
(I think) the patched apk is here
#### Howto
- Download Mevo APK
- `apktool`: decompile it
- it's all smali, cry about it
- Find a function which parses JSON command payloads -- unfortunately I forgot where this is!
- Patch smali: Insert android native log call -> the json payload
- re-compile it with apktool
- sign it + `adb push`
- `adb log` while running it
- see the commands
