#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

# Author: David Arroyo Menéndez <davidam@gmail.com>
# Maintainer: David Arroyo Menéndez <davidam@gmail.com>

# This file is free software; you can redistribute it and/or modify
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


import requests
import json
import os
from app.dame_gender import Gender

class DameBrazilApi(Gender):

    def get(self, name):
        # it allows to download a name from Brazil API
        v = {}
        v['name'] = name
        string = 'https://servicodados.ibge.gov.br/api/v2/censos/nomes/' + name
        string = string + "?sexo=F"
        r = requests.get(string)
        j = json.loads(r.text)
        count = 0
        try:
            for i in j[0]['res']:
                if (i['periodo'] == "[2000,2010["):
                    count = i['frequencia']
        except:
            count = 0
        v['females'] = count
        string2 = 'https://servicodados.ibge.gov.br/api/v2/censos/nomes/' + name
        string2 = string2 + "?sexo=M"
        r2 = requests.get(string2)
        j2 = json.loads(r2.text)
        count = 0
        try:        
            for i in j2[0]['res']:
                if (i['periodo'] == "[2000,2010["):
                    count = i['frequencia']
        except:
            count = 0
        v['males'] =  count
        if (v['males'] > v['females']):
            v['gender'] = 'male'
        else:
            v['gender'] = 'female'
        return v

    def download(self, path="files/names/partial.csv", *args, **kwargs):
        # download a json of people's names from a csv given
        backup = kwargs.get('backup', 'files/names/brazilnames.json')
        name_position = kwargs.get('name_position', 0)
        names = self.csv2names(path, name_position=name_position)
        jsondict = {}
        jsondict['names'] = []
        if backup:
            backup = open(backup, "w+")
        for i in names:
            name = self.get(i)
            jsondict['names'].append(name)
        jsonv = json.dumps(jsondict)
        backup.write(jsonv)
        backup.close()
        return 1

    def guess(self, name, binary=False):
        # returns a gender from a name
        v = self.get(name)
        guess = v['gender']
        if (guess == 'male'):
            if binary:
                guess = 1
        elif (guess == 'female'):
            if binary:
                guess = 0
        else:
            if binary:
                guess = 2
            else:
                guess = 'unknown'
        return guess

    def accuracy(self, name):
        v = self.get(name)
        if (v['males'] > v['females']):
            acc = v['males'] / (v['males'] + v['females'])
        else:
            acc = v['females'] / (v['males'] + v['females'])
        return acc