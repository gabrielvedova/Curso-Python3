import sys
from cx_Freeze import setup, Executable

build_exe_options = {"includes": [
    "tkinter", "random", "sys"], "include_files": ["imagens/icone.ico"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Gerador de Temas",
    version="1.0",
    description="Cria temas aleatórios para desenhos ou textos!",
    options={"build_exe": build_exe_options},
    executables=[Executable(script="tema_aleatório.py",
                            base=base, icon="icone.ico")]
)
