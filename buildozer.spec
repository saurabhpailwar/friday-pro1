[app]
title = FRIDAY PRO
package.name = fridaypro
package.domain = com.saurabh.friday
source.dir =.
source.include_exts = py,png
version = 1.0
requirements = python3,kivy,pyjnius
orientation = portrait

[buildozer]
log_level = 2

[app:permissions]
android.permissions = INTERNET,RECORD_AUDIO

[app:android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True
