#!/usr/bin/python

execfile("source/conf.py")

f = open("output/html/version.txt", "w")

f.write( """#QGIS Version %(versionint)d|Visit http://download.qgis.org to get your copy of version %(version)s|<html><body>
<ul>
<li>The current released version of QGIS is %(version)s.
<li>We are working on %(devversion)s-Master. It will go into feature freeze on %(freezedate)s and be released as %(nextversion)s on %(nextreleasedate)s.
<li>Details on changes can be found by examining the Activity in Redmine at <a href="http://hub.qgis.org/projects/quantum-gis">http://hub.qgis.org/projects/quantum-gis</a>.
</body>
</html>
""" % {
	"versionint": int("%d%02d%02d" % tuple( map(int, release.split(".")))),
	"version": release,
	"devversion": devversion,
	"freezedate": nextfreezedate,
	"nextreleasedate": nextreleasedate,
	"nextversion": nextversion,
} )

f.close()
