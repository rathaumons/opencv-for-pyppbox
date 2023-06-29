# GitHub: https://github.com/rathaumons/opencv-for-pyppbox
# Copyright (C) 2023 rathaROG

import io
import os
import os.path
import sysconfig
from setuptools import setup


def main():

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    install_requires = [
        'numpy>=1.24.4; python_version=="3.11.*"'
    ]

    version = set_version()
    print("VERSION=" + str(version))

    package_name = "pyppbox-opencv"

    long_description = io.open("README.md", encoding="utf-8").read()

    packages = ["cv2", "cv2.data", "cv2.gapi", "cv2.mat_wrapper", "cv2.misc", "cv2.python-3", "cv2.utils"]

    package_data = {
        "cv2": ["*%s" % sysconfig.get_config_vars().get("SO")]
        + (["*.dll"] if os.name == "nt" else [])
        + ["LICENSE.txt", "LICENSE-3RD-PARTY.txt"],
        "cv2.data": ["*.xml"],
        "cv2.gapi": ["*.*"],
        "cv2.mat_wrapper": ["*.*"],
        "cv2.misc": ["*.*"],
        "cv2.python-3": ["*.*"],
        "cv2.utils": ["*.*"],
    }

    setup(
        name=package_name,
        version=version,
        url="https://github.com/rathaumons/opencv-for-pyppbox",
        license="MIT",
        description="Wrapper package for OpenCV python bindings.",
        long_description=long_description,
        long_description_content_type="text/markdown",
        packages=packages,
        package_data=package_data,
        maintainer="rathaROG",
        install_requires=install_requires,
        python_requires="==3.11.*",
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "Intended Audience :: Education",
            "Intended Audience :: Information Technology",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: MIT License",
            "Operating System :: Microsoft :: Windows",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3 :: Only",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: C++",
            "Programming Language :: Python :: Implementation :: CPython",
            "Topic :: Scientific/Engineering",
            "Topic :: Scientific/Engineering :: Image Recognition",
            "Topic :: Software Development",
        ],

    )

def set_version():
    version = {}
    here = os.path.abspath(os.path.dirname(__file__))
    version_file = os.path.join(here, "version.txt")
    with open(version_file) as fp:
        exec(fp.read(), version)
    return version["opencv_version"]


def set_wheel_tags(force=True):
    if force:
        import sys
        sys.argv.extend(['--python-tag', 'cp311'])
        sys.argv.extend(['--plat-name', 'win_amd64'])

if __name__ == "__main__":
    set_wheel_tags()
    main()
