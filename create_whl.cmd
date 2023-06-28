::    GitHub: https://github.com/rathaumons/opencv-for-pyppbox
::    Copyright (C) 2023 rathaROG

@echo off
setlocal
cd /d %~dp0
set "PYTHONWARNINGS=ignore"
python -m pip install --upgrade pip
pip install wheel build
python -m build --wheel --skip-dependency-check --no-isolation
pause