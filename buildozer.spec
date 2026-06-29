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

# Android налаштування
android.build_tools_version = 33.0.2
android.api = 33
android.minapi = 21
android.archs = arm64-v8a
android.ndk = 25b
p4a.branch = release-2023.09.16

# дозволи (ти сказав без інтернету — тому мінімально)
android.permissions =

# інші налаштування
android.allow_backup = True
android.private_storage = True

[buildozer]

log_level = 2
warn_on_root = 1
