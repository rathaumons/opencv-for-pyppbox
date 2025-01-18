# GitHub: https://github.com/rathaumons/opencv-for-pyppbox
# Copyright (C) 2024 rathaROG

import io
import os
import os.path
from setuptools import find_packages, find_namespace_packages, setup


def main():

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    package_name = "pyppbox-opencv"
    long_description = io.open("README.md", encoding="utf-8").read()
    version = set_version()
    packages = find_packages() + find_namespace_packages(where='.', include=['cv2.*'])
    packages = list(set(packages))
    package_data = {}
    for p in packages:
        package_data.update({p: ["*"]})

    install_requires = [
        'numpy>=1.26.4; python_version=="3.9.*"'
    ]

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
        include_package_data=True,
        maintainer="rathaROG",
        install_requires=install_requires,
        python_requires="==3.9.*",
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
            "Programming Language :: Python :: 3.9",
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
        sys.argv.extend(['--python-tag', 'cp39'])
        sys.argv.extend(['--plat-name', 'linux_x86_64'])

if __name__ == "__main__":
    set_wheel_tags()
    main()
