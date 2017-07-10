#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import csv

url = "https://docs.google.com/spreadsheets/u/1/d/1MOIjwon5eDI04DG6rX_HwucZkW1fxFJ0b_yB0xYETOE/export?format=csv&id=1MOIjwon5eDI04DG6rX_HwucZkW1fxFJ0b_yB0xYETOE&gid=1982100417#"

o = open("source/site/getinvolved/development/schedule.inc", "w")

o.write("""\
========== ======= ========= ===== ========== ==== =====
Event      Latest  Long-Term  FF   Date       Week Weeks
                   Repo                       #
========== ======= ========= ===== ========== ==== =====
""")

csvfile = urllib2.urlopen(url)
reader = csv.reader(csvfile, delimiter=',', quotechar='"')
first = True
for row in reader:
    if first:
        first = False
        continue

    event, _, _, _,  _, _, _,  _, _, date, weekno, weeks, lr, ltr, dev, _, _, _, _ = row

    event = event.replace('LR', '**LR**')
    event = event.replace('LTR', '**LTR**')

    o.write("{0:10s} {1:7s} {2:9s} {3:5s} {4:10s} {5:5s} {6}\n".format(event, lr, ltr, dev, date, weekno, weeks))

csvfile.close()

o.write("""\
========== ======= ========= ===== ========== ==== =====
""")

o.close()
