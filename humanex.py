# setup.py
from cx_Freeze import setup, Executable

setup(
    name="Humanex",
    version="14.0",
    description="Browser Simulator",
    executables=[Executable("Humanex14.0.py", base="Win32GUI", icon="favicon.ico")],
)
