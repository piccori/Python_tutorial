import os


PROJECT_DIR = 'C:¥python-izm'
SETTING_FILE = 'settings.ini'
# pathの結合・連結
print(os.path.join(PROJECT_DIR, SETTING_FILE))
print(os.path.join(PROJECT_DIR, 'settings_dir', SETTING_FILE))
