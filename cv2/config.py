# GitHub: https://github.com/rathaumons/opencv-for-pyppbox
# Copyright (C) 2023 rathaROG

import os

BINARIES_PATHS = [
    # os.path.join(os.getenv('CUDA_PATH', 'C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v12.1'), 'bin')
    os.path.join(os.path.dirname(os.path.abspath(os.path.realpath(__file__))), 'cuda_bin')
] + BINARIES_PATHS
