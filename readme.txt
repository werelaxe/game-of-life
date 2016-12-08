Game of life

Requirements:
    Python 3.x (only 32-bit!) with installed module PyOpenGL
    For Windows is dll for OpenGL (glut32.dll)

General usage:
    For using program just run main.py or run script in console:
    python main.py [options] [arguments] for windows
    python3 main.py [options] [arguments] for linux-based OS

Installing:
    Linux-based:
        1) Install python 3.x, 32-bit version
        2) Then just type "sudo apt-get install python3-opengl"
    Windows:
        1) Install python 3.x, 32-bit version
        2) Install python module "PyOpenGL" (with pip type "pip install PyOpenGL")
        3) Donwload and copy glut32.dll to main script directory or to %windir%\System32

Controlling:
use
    SPACE for pause/strop iterations
    C for clean all cells
    R for randomizate field
    ESCAPE for exit