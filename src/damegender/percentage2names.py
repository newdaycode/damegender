#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2022  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

# Author: David Arroyo Menéndez <davidam@gmail.com>
# Maintainer: David Arroyo Menéndez <davidam@gmail.com>

# This file is Free Software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with DameGender; see the file GPL.txt.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

# DESCRIPTION
# Given a percentage and a country give me the names

from app.dame_gender import Gender
from app.dame_utils import DameUtils
import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument("percentage_from")
parser.add_argument("--percentage_until", default=-1)
parser.add_argument('--total', default="inter",
                    choices=['at', 'au', 'be', 'ca', 'ch',
                             'cn', 'de', 'dk', 'es', 'fi',
                             'fr', 'gb', 'ie', 'is', 'no', 'nz',
                             'mx', 'pt', 'ru', 'se', 'si', 'tr',
                             'uy', 'us', 'inter'])
# More about iso codes on https://www.iso.org/obp/ui/
parser.add_argument('--version', action='version', version='0.4')
args = parser.parse_args()

g = Gender()
du = DameUtils()
dicc0 = du.dicc_dataset("all")
print(dicc0)
path = dicc0[args.total]
print(path)
if (args.percentage_until == -1):
    percentage_until = float(args.percentage_from)
elif (args.percentage_from > args.percentage_until):
    percentage_until = float(args.percentage_from)
else:
    percentage_until = float(args.percentage_until)

percentage_from = float(args.percentage_from)

with open(path) as csvfile:
    sreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in sreader:
        try:
            males = round(float(row[3]))
        except IndexError:
            print("The program has troubles with some array indexes")

        if ((males >= percentage_from) and (males <= percentage_until)):
            print(row[0] + "," + str(males) + ",M")
            
        try:
            females = round(float(row[2]))
        except IndexError:
            print("The program has troubles with some array indexes")            

        if ((females >= percentage_from) and (females <= percentage_until)):
            print(row[0] + "," + str(females) + ",F" )
