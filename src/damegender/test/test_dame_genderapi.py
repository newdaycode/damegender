#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

#  Author: David Arroyo Menéndez <davidam@gmail.com>
#  Maintainer: David Arroyo Menéndez <davidam@gmail.com>

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.


import unittest
import os
import requests
import json
from app.dame_genderapi import DameGenderApi
from app.dame_utils import DameUtils


class TddInPythonExample(unittest.TestCase):

    def test_dame_genderapi_get(self):
        dga = DameGenderApi()
        if (dga.config['DEFAULT']['genderapi'] == 'yes'):
            v = dga.get("Diana")
            self.assertEqual(v[0], "female")
            self.assertTrue(v[1] > 90)
            self.assertEqual(len(v), 2)

    def test_dame_genderapi_guess(self):
        dga = DameGenderApi()
        if (dga.config['DEFAULT']['genderapi'] == 'yes'):
            g = dga.guess("Sara", binary=False)
            self.assertEqual(g, "female")
            g = dga.guess("Paula", binary=False)
            self.assertEqual(g, "female")
            g = dga.guess("Sara", binary=True)
            self.assertEqual(g, 0)

    def test_dame_genderapi_download(self):
        dga = DameGenderApi()
        du = DameUtils()
        path1 = "files/names/min.csv"
        if (dga.config['DEFAULT']['genderapi'] == 'yes'):
            g = dga.download(path1)
            self.assertTrue(
                os.path.isfile(
                    "files/names/genderapi"+du.path2file(path1)+".json"))

    def test_dame_genderapi_accuracy(self):
        dga = DameGenderApi()
        if (dga.config['DEFAULT']['genderapi'] == 'yes'):
            acc = dga.accuracy("Diana")
            self.assertTrue(acc > 90)

    def test_dame_genderapi_guess_list(self):
        dga = DameGenderApi()
        if (dga.config['DEFAULT']['genderapi'] == 'yes'):
            self.assertEqual(['male', 'male', 'male', 'male', 'male', 'female'],
                             dn.guess_list(path="files/names/partial.csv",
                                      binary=False))
            self.assertEqual([1, 1, 1, 1, 1, 0],
                             dn.guess_list(path="files/names/partial.csv",
                                      binary=True))

    def test_dame_genderapi_json2gender_list(self):
        dga = DameGenderApi()
        if (dga.config['DEFAULT']['genderapi'] == 'yes'):
            self.assertEqual(['male', 'male', 'male', 'male'],
                             dga.json2gender_list(
                                 jsonf="files/names/genderapifiles_names_min.processed.json"))
            self.assertEqual([1, 1, 1, 1],
                             dga.json2gender_list(
                                 jsonf="files/names/genderapifiles_names_min.processed.json",
                                 binary=True))

    def test_dame_genderapi_confusion_matrix_gender(self):
        dga = DameGenderApi()
        if (dga.config['DEFAULT']['genderapi'] == 'yes'):
            cm = dga.confusion_matrix_gender(path="files/names/min.csv",
                                         dimensions="2x3")
            am = [[1, 0, 0], [0, 5, 0]]
            self.assertEqual(cm, am)

    def test_dame_gender_check_names(self):
        g = DameGenderApi()
        self.assertTrue(g.json_eq_csv_in_names(jsonf="files/names/genderapifiles_names_min.csv.json", path="files/names/min.csv"))
