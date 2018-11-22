#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2018  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with GNU Emacs; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

from app.sexmachine import Sexmachine
from app.gendergit import GenderGit
import sys
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("url", help="Uniform Resource Link")
parser.add_argument('--directory')
parser.add_argument('--version', action='version', version='0.1')
args = parser.parse_args()
if (len(sys.argv) > 1):
    s = Sexmachine()
    gg = GenderGit()
    l1 = gg.list_committers(args.url, args.directory)
    l2 = gg.delete_duplicated(l1)

    females = 0
    males = 0
    unknowns = 0
    for g in l2:
        sm = s.guess(g, binary=True)
        if (sm == 0):
            females = females + 1
        elif (sm == 1):
            males = males + 1
        else:
            unknowns = unknowns + 1

    print("The number of males sending commits is %s" % males)
    print("The number of females sending commits is %s" % females)
