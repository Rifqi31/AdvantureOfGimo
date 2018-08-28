import sys
import cx_Freeze
from cx_Freeze import setup, Executable

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="Advanture Of Gimo",
    version="1.0",
    description="Education Game for lean Hiragana & Katakana",
    author="Rifqi Muttaqin",
    author_email="muttaqinrifqi31@gmail.com",
    url="https://github.com/Rifqi31/AdvantureOfGimo",
        options={"build_exe": {"packages": ["pygame"], "include_files": [
            "spritesheet/", "sounds/", "pygameMenu/fonts/", "fonts/"]}},
    executables=executables
)
