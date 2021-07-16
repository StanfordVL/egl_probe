"""
NOTE: this is adapted from https://github.com/StanfordVL/iGibson/blob/master/setup.py
"""
import os
import sys
import shutil
import subprocess
from setuptools import setup, find_packages


def build_cmake():
    try:
        out = subprocess.check_output(['cmake', '--version'])
    except OSError:
        raise RuntimeError("CMake must be installed.")

    # make build directory
    here = os.path.abspath(os.path.dirname(__file__))
    build_dir = os.path.join(here, "egl_probe", "build")
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
    os.mkdir(build_dir)

    # build using cmake
    subprocess.check_call("cd egl_probe/build; cmake ..; make -j", shell=True)

if sys.version_info.major == 3:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
else:
    # for python2
    with open("README.md", "r") as fh:
        long_description = fh.read()

build_cmake()
setup(
    name='egl_probe',
    version='1.0.0',
    author='Stanford University',
    url='https://github.com/StanfordVL/egl_probe',
    zip_safe=False,
    packages=find_packages(),
    install_requires=[],
    tests_require=[],
    include_package_data=True,
    long_description=long_description,
    long_description_content_type='text/markdown'
)   #yapf: disable
