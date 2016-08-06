#!/usr/bin/env python

import argparse
import os
import os.path
import tarfile
import shutil

def main():
    package_name = "uClibc++-0.2.4"
    file_name = "%s.tar.bz2" % package_name

    if not os.path.exists("src"):
        shutil.rmtree("./src", ignore_errors=True)
        os.makedirs("src")

    if not os.path.exists("__build__"):
        os.makedirs("__build__")
    os.chdir("__build__")

    if not os.path.exists(file_name):
        os.system("wget https://git.busybox.net/uClibc++/snapshot/%s" % file_name)

    with tarfile.open(file_name, "r:bz2") as atarfile:
        atarfile.extractall()

    os.system("cp -rf ./%s/src/* ../src" % package_name)
    os.system("cp -rf ./%s/include/* ../src" % package_name)
    os.system("cp -rf ../patch_src/* ../src")

    os.remove("../src/support.cpp")

    with open("../src/memory", "a") as afile:
        afile.write('\n#include "patches/memory"\n')

    with open("../src/stdexcept", "a") as afile:
        afile.write('\n#include "patches/exception"\n')

if __name__ == "__main__":
    main()