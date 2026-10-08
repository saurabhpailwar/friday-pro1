[app]
title = FRIDAY PRO AI
package.name = fridaypro1
package.domain = com.saurabhpailwar.fridaypro1
source.dir = .
source.include_exts = py,png,jpg
version = 1.0
requirements = python3,kivy,pyjnius,requests
orientation = portrait
fullscreen = 0
icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/logo.png
android.permissions = INTERNET,RECORD_AUDIO,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,MODIFY_AUDIO_SETTINGS
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True
android.ant = auto
p4a.bootstrap = sdl2

[buildozer]
log_level = 2
