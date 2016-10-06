rmdir /s /q release
del /q atImage.spec

pyinstaller --workpath=release\build --distpath=release -F -w --icon="images\atImage.ico" atImage.py

