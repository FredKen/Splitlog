#!/usr/bin/env python3

import os
import glob
import json

for ficDeal in glob.glob('/home/fredken/scripts/*.json'):
    with open(ficDeal) as f:
        deal = json.load(f)
        #deal = {"one":"Some data", "two":"Some data"}
        print(deal[1])
        i = 0
        for item in deal:
            name = str(i) + '.json'
            file = open(name, 'w')
            file.write('{"%s"}' % (deal[item]))
            file.close()