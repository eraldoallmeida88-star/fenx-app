[app]

# (str) Title of your application
title = Fênx infoShop

# (str) Package name
package.name = fenxinfoshop

# (str) Package domain (needed for android packaging)
package.domain = org.fenx

# (str) Source directory where the application lives
source.dir = .

# (str) Application versioning (version numbering)
version = 0.1

# (list) Source files to include (letting it know about the excel spreadsheet)
source.include_exts = py,png,jpg,kv,atlas,xlsx

# (list) Source files to exclude (letting it know to exclude unnecessary files)
source.exclude_exts = spec

# (list) List of directory to exclude
source.exclude_dirs = bin, venv, .git, .github

# (list) List of exclusions
source.exclude_patterns = license, images/*.jpg

# (list) Specify the inclusion pattern for files/directories
source.include_patterns = CODIGO VS ENGENHARIA.xlsx

# (list) Application requirements
# Inclui o Python 3, Kivy, Pandas, Openpyxl e NumPy para leitura e processamento offline da planilha
requirements = python3,kivy,pandas,openpyxl,numpy

# (str) Supported orientations
orientation = portrait

# (list) List of service to declare
#services = 

#
# OSX Specific
#

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Preslash for Android sdk (e.g. --sdk_version)
android.sdk = 33

# (string) The Android min API version
android.min_api = 21

# (string) The Android target API version
android.target_api = 33

# (str) Android architectural build types (arm64-v8a is required for modern Android devices)
android.archs = arm64-v8a

# (bool) Use AndroidX for support libraries
android.androidx = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_root = 1
