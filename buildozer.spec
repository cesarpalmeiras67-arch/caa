[app]
title = Minha Comunicação - CAA
package.name = comunicacao
package.domain = org.caa
source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,atlas,ttf,otf
version = 1.0.0

requirements = python3,kivy==2.3.0,pyjnius

orientation = portrait
fullscreen = 0

android.api = 35
android.minapi = 23
android.ndk = 27c
android.accept_sdk_license = True

android.permissions = INTERNET

# Mantém o projeto simples e permite usar a API nativa de voz do Android.
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
