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
android.api = 33
android.minapi = 21
android.archs = arm64-v8a

# дозволи (ти сказав без інтернету — тому мінімально)
android.permissions =

# інші налаштування
android.allow_backup = True
android.private_storage = True

[buildozer]

log_level = 2
warn_on_root = 1
