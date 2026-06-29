[app]

title = Clicker
package.name = clicker
package.domain = org.clicker

source.dir = .
source.include_exts = py,kv,png,jpg,ttf,mp3,ogg,json

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

# Android settings (СТАБІЛЬНІ)
android.api = 33
android.minapi = 21
android.archs = arm64-v8a

# ФІКС ВЕРСІЇ (важливо)
android.build_tools_version = 33.0.2
android.ndk = 25b


p4a.branch = master

[buildozer]

log_level = 2
warn_on_root = 1
