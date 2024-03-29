# GitHub: https://github.com/rathaumons/opencv-for-pyppbox
# Copyright (C) 2024 rathaROG

import cv2


def get_ocv_version():
    return getattr(cv2, "__version__", "4.8.1.101+cu121")
