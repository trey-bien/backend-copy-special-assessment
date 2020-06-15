#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "Trey Dickerson with the immeasurable help of Stack Overflow"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""

    files = os.listdir(dirname)
    result = []

    for file in files:
        match = re.search(r'__(\w+)__', file)
        if match:
            result.append(os.path.abspath(os.path.join(dirname, file)))

    return result


def copy_to(path_list, dest_dir):

    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
    for path in path_list:
        file = os.path.basename(path)
        shutil.copy(path, os.path.join(dest_dir, file))


def zip_to(path_list, dest_zip):
    
    files = ''
    for path in path_list:
        files += path + ' '
    print("Command about to be executed:")
    print('zip -j', dest_zip, files)
    try:
        subprocess.call(['zip', '-j', dest_zip] + path_list)
    except OSError as e:
        print(e)
        exit(1)
    return


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')

    # TODO: add one more argument definition to parse the 'from_dir' argument
    parser.add_argument('fromdir', help='')

    ns = parser.parse_args(args)

    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    if not ns:
        parser.print_usage()
        sys.exit(1)
    
    special_paths = get_special_paths(ns.fromdir)

    if ns.todir:
        copy_to(special_paths, ns.todir)
    if ns.tozip:
        zip_to(special_paths, ns.tozip)
    
    if not ns.todir and not ns.tozip:
        for path in special_paths:
            print(path)

if __name__ == "__main__":
    main(sys.argv[1:])
