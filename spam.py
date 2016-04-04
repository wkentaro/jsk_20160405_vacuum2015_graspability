#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


lines = open('a.csv').readlines()
header = 'Item,ApproxWeight,Unit,CountryofOrigin'
csv_lines = [header]
for line in lines[1:]:
    line = line.strip()
    m = re.match('(.*) ([0-9]*\.?[0-9]*) (oz|lbs) (.*)', line)
    name, weight, unit, origin = m.groups()

    name = name.replace(' ', '_').lower()
    name = name.replace('&', 'and')
    name = name.replace('-', '_')
    name = name.replace("'", '')
    name = name.replace('.', '')
    name = name.replace('#', 'number')
    csv_lines.append(','.join([name, weight, unit, origin]))
open('out.csv', 'w').write('\n'.join(csv_lines))