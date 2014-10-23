#!/usr/bin/env python2.7
from __future__ import division, print_function

import sys, os, platform, os.path
import glob, shutil
import subprocess
import distutils.sysconfig
import fnmatch

def remove(patterns):
    matches = set()
    for root, dirs, files in os.walk("."):
        for pattern in patterns:
            for filename in fnmatch.filter(files, pattern):
                matches.add(os.path.join(root, filename))

    for filename in matches:
        try: os.remove(filename)
        except: pass

def printUsage():
    print("Usage:")
    print("    python make.py <command>")
    print("Commands:")
    print("    build - builds PyGG2's extensions")
    print("    clean - cleans up Python bytecode files and build remains")

if len(sys.argv) == 1:
    printUsage()
    sys.exit()

if sys.argv[1] == "build":
    if len(sys.argv) > 2 and sys.argv[2] == "dist":
        if platform.system() == "Windows":
            import build_win
            sys.argv = sys.argv[:2]
            build_win.build()
        else:
            print(platform.system() + " not supported.")
    else:
        includes = distutils.sysconfig.get_python_inc()

        if platform.system() == "Linux":
            subprocess.call("gcc -fPIC -O3 -c -o mask_extension/bitmask.o mask_extension/bitmask.c", shell=True)
            subprocess.call("gcc -I%s -fPIC -O3 -c -o mask_extension/_mask.o mask_extension/_mask.c" % includes, shell=True)
            subprocess.call("gcc -shared -o mask_extension/_mask.so mask_extension/bitmask.o mask_extension/_mask.o", shell=True)
        else:
            libs = os.path.join(os.path.join(includes, ".."), "libs")
            subprocess.call("gcc -O3 -c -o mask_extension/bitmask.o mask_extension/bitmask.c", shell=True)
            subprocess.call("gcc -I%s -O3 -c -o mask_extension/_mask.o mask_extension/_mask.c" % includes, shell=True)
            subprocess.call("gcc -shared -o mask_extension/_mask.pyd mask_extension/bitmask.o mask_extension/_mask.o -L%s -lpython27" % libs, shell=True)
elif sys.argv[1] == "clean":
    patterns = [
        "*~",
        "*.pyc",
        "*.pyo",
        "*.o",
        "game_profile",
        "profile.txt"
    ]
    remove(patterns)
    try: shutil.rmtree("dist")
    except: pass