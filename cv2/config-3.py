# GitHub: https://github.com/rathaumons/opencv-for-pyppbox
# Copyright (C) 2024 rathaROG

import os

PYTHON_EXTENSIONS_PATHS = [
    os.path.join(os.path.dirname(os.path.abspath(os.path.realpath(__file__))), 'python-3')
] + PYTHON_EXTENSIONS_PATHS
