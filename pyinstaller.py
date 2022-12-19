import PyInstaller.__main__

# pyinstaller --noconfirm --onedir --windowed --add-data "<CustomTkinter Location>/customtkinter;customtkinter/"  "<Path to Python Script>"

PyInstaller.__main__.run([
    "--noconfirm",
    "--onedir",
    "--windowed",
    "--add-data=\"../../../../../AppData/Local/Packages/PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0/LocalCache/local-packages/Python310/site-packages/customtkinter;customtkinter/\"",
    "autoclickerV2.py"
])