# GitHub: https://github.com/rathaumons/opencv-for-pyppbox
# Copyright (C) 2023 rathaROG

import os

BINARIES_PATHS = [
    os.path.join(os.getenv('CUDA_PATH', 'C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v11.8'), 'bin')
] + BINARIES_PATHS
