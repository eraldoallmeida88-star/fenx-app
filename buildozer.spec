[app]

title = Fenx infoShop
package.name = fenxinfoshop
package.domain = org.fenx
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,xlsx
source.include_patterns = CODIGO VS ENGENHARIA.xlsx
version = 1.0
requirements = python3,kivy,pyjnius
orientation = portrait
fullscreen = 0
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.build_tools_version = 33.0.0
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
