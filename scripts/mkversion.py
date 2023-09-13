#!/usr/bin/python

import json

exec(open("source/schedule.py").read())

with open("output/html/version.txt", "w") as f:
    f.write("""#QGIS Version %(versionint)d|Visit https://download.qgis.org to get your copy of version %(version)s|<html><body>
<ul>
<li>The current released version of QGIS is %(version)s.
<li>We are working on %(devversion)s-Master. It will go into feature freeze on %(freezedate)s and be released as %(nextversion)s on %(nextreleasedate)s.
<li>Details on changes can be found on github at <a href="https://github.com/qgis/QGIS/commits/master">https://github.com/qgis/QGIS/commits/master</a>.
</body>
</html>
""" % {
        "versionint": int("%d%02d%02d" % tuple(map(int, release.split(".")))),
        "version": release,
        "devversion": devversion,
        "freezedate": nextfreezedate if nextfreezedate is not None else "a not yet determined date",
        "nextreleasedate": nextreleasedate if nextreleasedate is not None else "a not yet determined date",
        "nextversion": nextversion,
    })

with open("output/html/version-ltr.txt", "w") as f:
    f.write("""#QGIS Version %(versionint)d|Visit https://download.qgis.org to get your copy of version %(ltrversion)s|<html><body>
<ul>
<li>The current available LTR version of QGIS is %(ltrversion)s.
<li>The latest available version of QGIS is %(version)s.
<li>We are working on %(devversion)s-Master. It will go into feature freeze on %(freezedate)s and be released as %(nextversion)s on %(nextreleasedate)s.
<li>Details on changes can be found on github at <a href="https://github.com/qgis/QGIS/commits/master">https://github.com/qgis/QGIS/commits/master</a>.
</body>
</html>
""" % {
	    "versionint": int("%d%02d%02d" % tuple(map(int, ltrrelease.split(".")))),
	    "ltrversion": ltrrelease,
        "version": release,
	    "devversion": devversion,
	    "freezedate": nextfreezedate if nextfreezedate is not None else "a not yet determined date",
	    "nextreleasedate": nextreleasedate if nextreleasedate is not None else "a not yet determined date",
	    "nextversion": nextversion,
    } )

with open("output/html/version.json", "w") as f:
    json.dump({
        'latest': {
            'versionint': int("%d%02d%02d" % tuple(map(int, release.split(".")))),
            'version': release,
            'name': codename,
            'note': releasenote,
            'binary': binary,
            'date': releasedate.strftime('%Y-%m-%d'),
            'major': int(release.split(".")[0]),
            'minor': int(release.split(".")[1]),
            'patch': int(release.split(".")[2])
        },
        'ltr': {
            'versionint': int("%d%02d%02d" % tuple(map(int, ltrrelease.split(".")))),
            'version': ltrrelease,
            'name': ltrcodename,
            'note': ltrnote,
            'binary': ltrbinary,
            'date': releasedate.strftime('%Y-%m-%d'),
            'major': int(ltrrelease.split(".")[0]),
            'minor': int(ltrrelease.split(".")[1]),
            'patch': int(ltrrelease.split(".")[2])
        },
        'dev': {
            'version': devversion,
            'versionint': int("%d%02d00" % tuple(map(int, devversion.split(".")))),
            'major': int(devversion.split(".")[0]),
            'minor': int(devversion.split(".")[1]),
            'patch': 0
        },
        'freezedate': nextfreezedate if nextfreezedate is not None else "a not yet determined date",
	    "nextreleasedate": nextreleasedate if nextreleasedate is not None else "a not yet determined date",
	    "nextversion": nextversion,
    }, f, indent=4)
