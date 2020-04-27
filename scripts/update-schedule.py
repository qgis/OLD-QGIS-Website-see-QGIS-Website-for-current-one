#!/usr/bin/python
# -*- coding: utf-8 -*-

from urllib.request import urlopen
import csv
import codecs
from datetime import datetime, timedelta, timezone
from icalendar import Calendar, Event

url = "https://docs.google.com/spreadsheets/u/1/d/1MOIjwon5eDI04DG6rX_HwucZkW1fxFJ0b_yB0xYETOE/export?format=csv&id=1MOIjwon5eDI04DG6rX_HwucZkW1fxFJ0b_yB0xYETOE&gid=1982100417#"

o = open("source/site/getinvolved/development/schedule.inc", "w")

o.write("""\
.. produced from googlesheet via scripts/update-schedule.py - edits will be lost

========== ======= ========= ======== ========== ==== =====
Event      Latest  Long-Term  Freeze   Date      Week Weeks
                   Repo                          #
========== ======= ========= ======== ========== ==== =====
""")

cal = Calendar()
cal.add('prodid', '-//Release Schedule//qgis.org//')
cal.add('version', '2.0')
cal['summary'] = 'QGIS Release Schedule'

resource = urlopen(url)
reader = csv.reader(codecs.iterdecode(resource, 'utf-8'), delimiter=',', quotechar='"')
first = True
f_date = None
pr_date = None
nr_date = None

ltr_version = None
lr_version = None
lr_is_ltr = False
lr_date = None

for row in reader:
    if first:
        first = False
        continue

    event, _, _, _,  _, _, _,  _, _, date, weekno, weeks, lr, ltr, dev, ff, _, _ = row

    dt = datetime.strptime(date, '%Y-%m-%d').replace(tzinfo=timezone.utc) + timedelta(hours=12)

    if 'FF' in event:
        e = Event()
        e.add('summary', 'QGIS Feature Freeze {}'.format(dev))
        e.add('dtstart', dt)
        e.add('dtend', dt)
        cal.add_component(e)

    if 'SF' in event:
        e = Event()
        e.add('summary', 'QGIS Soft Freeze', dev)
        e.add('dtstart', dt)
        e.add('dtend', dt)
        cal.add_component(e)

    if 'PR' in event:
        label = 'Extra point release' if 'EPR' in event else 'Point release'
        if ltr and 'LTR' not in event:
            e = Event()
            e.add('summary', 'QGIS {} {}'.format(label, ltr))
            e.add('dtstart', dt)
            e.add('dtend', dt)
            cal.add_component(e)

        if lr and 'LR' not in event:
            e = Event()
            e.add('summary', 'QGIS {} {}'.format(label, lr))
            e.add('dtstart', dt)
            e.add('dtend', dt)
            cal.add_component(e)

    if 'LTR' in event and ltr:
        e = Event()
        e.add('summary', 'QGIS Long-term release {}'.format(ltr))
        e.add('dtstart', dt)
        e.add('dtend', dt)
        cal.add_component(e)

    if 'LR' in event and ltr:
        e = Event()
        e.add('summary', 'QGIS Regular release {}'.format(lr))
        e.add('dtstart', dt)
        e.add('dtend', dt)
        cal.add_component(e)

    if ("FF" in event or "SF" in event) and nr_date is None:
       f_date = dt

    if dt > datetime.now(timezone.utc).replace(hour=12, minute=0, second=0):
        if "PR" in event and pr_date is None:
            pr_date = dt

        if ("LR" in event or "LTR" in event) and nr_date is None:
            nr_date = dt
    else:
        ltr_version = ltr
        lr_version = lr
        lr_date = dt

    event = event.replace('LR', '**LR**')
    event = event.replace('LTR', '**LTR**')

    o.write("{0:10s} {1:7s} {2:9s} {3:8s} {4:10s} {5:5s} {6}\n".format(event, lr, ltr, dev, date, weekno, weeks))

o.write("""\
========== ======= ========= ======== ========== ==== =====
""")

o.close()

url = "https://docs.google.com/spreadsheets/u/1/d/1MOIjwon5eDI04DG6rX_HwucZkW1fxFJ0b_yB0xYETOE/export?format=csv&id=1MOIjwon5eDI04DG6rX_HwucZkW1fxFJ0b_yB0xYETOE&gid=1060997136"

resource = urlopen(url)
reader = csv.reader(codecs.iterdecode(resource, 'utf-8'), delimiter=',', quotechar='"')

ltr_name = None
ltr_note = None
ltr_binary = None
lr_name = None
lr_note = None
lr_binary = None
devversion = None
nextversion = None

for row in reader:
    r, name, note, binary = row
    if r == "LTR":
        ltr_name, ltr_note, ltr_binary = name, note, binary
    elif r == "LR":
        lr_name, lr_note, lr_binary = name, note, binary
    elif r == "DEV":
        devversion = name
    elif r == "NEXT":
        nextversion = name

o = open("source/schedule.py", "w")

o.write("""\
from datetime import date

# latest release
version = '%(version)s'
release = '%(release)s'
codename = u'%(lr_name)s'
binary = '%(lr_binary)s'
releasedate = date(%(releasedate)s)
releasenote = u'%(lr_note)s'

# long term release repository
ltrversion = '%(ltrversion)s'
ltrrelease = '%(ltrrelease)s'
ltrcodename = u'%(ltr_name)s'
ltrbinary = '%(ltr_binary)s'
ltrnote = u'%(ltr_note)s'

devversion = '%(devversion)s'
nextversion = '%(nextversion)s'
nextfreezedate = '%(nextfreezedate)s'
nextreleasedate = '%(nextreleasedate)s'
nextpointreleasedate = '%(nextpointreleasedate)s'

infeaturefreeze = %(infeaturefreeze)s
""" % {
    "version": ".".join(lr_version.split(".")[:2]),
    "release": lr_version,
    "releasedate": "{0}, {1}, {2}".format(lr_date.year, lr_date.month, lr_date.day),
    "lr_binary": lr_binary,
    "lr_name": lr_name,
    "lr_note": lr_note,
    "lr_note": lr_note if lr_note != '' else '\\u200B',
    "ltrversion": ".".join(ltr_version.split(".")[:2]),
    "ltrrelease": ltr_version,
    "ltr_name": ltr_name,
    "ltr_binary": ltr_binary,
    "ltr_note": ltr_note if ltr_note != '' else 'LTR',
    "devversion": devversion,
    "nextversion": nextversion,
    "nextfreezedate": f_date.strftime('%Y-%m-%d %H:%M:%S UTC') if f_date is not None else None,
    "nextreleasedate": nr_date.strftime('%Y-%m-%d %H:%M:%S UTC') if nr_date is not None else None,
    "nextpointreleasedate": pr_date.strftime('%Y-%m-%d %H:%M:%S UTC'),
    "infeaturefreeze": "True" if f_date < datetime.now(timezone.utc).replace(hour=12, minute=0, second=0) else "False"
})

o.close()

o = open("output/html/schedule.ics", "wb")
o.write(cal.to_ical())
o.close()
