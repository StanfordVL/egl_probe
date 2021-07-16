"""
NOTE: this is adapted from https://github.com/StanfordVL/iGibson/blob/master/setup.py
"""
import os
import sys
import shutil
import subprocess
from setuptools import setup, Extension, find_packages
from setuptools.command.build_ext import build_ext


class CMakeExtension(Extension):
    def __init__(self, name, sourcedir=''):
        Extension.__init__(self, name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)


class CMakeBuild(build_ext):
    def run(self):
        try:
            out = subprocess.check_output(['cmake', '--version'])
        except OSError:
            raise RuntimeError("CMake must be installed.")

        for ext in self.extensions:
            self.build_extension(ext)

    def build_extension(self, ext):
        extdir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))

        # make build directory
        build_dir = os.path.join(extdir, "egl_probe", "build")
        if os.path.exists(build_dir):
            shutil.rmtree(build_dir)
        os.mkdir(build_dir)

        # build using cmake
        subprocess.check_call("cmake ..; make -j", cwd=build_dir, shell=True)


if sys.version_info.major == 3:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
else:
    # for python2
    with open("README.md", "r") as fh:
        long_description = fh.read()


setup(
    name='egl_probe',
    version='1.0.1',
    author='Stanford University',
    url='https://github.com/StanfordVL/egl_probe',
    zip_safe=False,
    packages=find_packages(),
    install_requires=[],
    ext_modules=[CMakeExtension('EGLProbe', sourcedir='egl_probe')],
    cmdclass=dict(build_ext=CMakeBuild),
    tests_require=[],
    include_package_data=True,
    long_description=long_description,
    long_description_content_type='text/markdown'
)   #yapf: disable
