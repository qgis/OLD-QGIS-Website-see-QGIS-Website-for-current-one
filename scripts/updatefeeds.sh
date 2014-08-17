
# script to be run on server serving the static content of the website
# doc root in /ar/www/qgis_new_web/QGIS-Website/live/html


# update planet first
#/home/web/qgis-django/update_planet.sh

mkdir -p /var/www/qgisdata/QGIS-Website/live/html/feeds
# cd to feed output dir
cd /var/www/qgisdata/QGIS-Website/live/html/feeds

# make backup
mv qgisflickrmaps.atom qgisflickrmaps.atom.0
# get latest qgis flickrmaps
curl "http://api.flickr.com/services/feeds/groups_pool.gne?id=2244553@N22&lang=en-us&format=atom" -o qgisflickrmaps.atom

# make backup
mv qgisflickrscreenshots.atom qgisflickrscreenshots.atom.0
# get latest qgis flickrscreenshots
curl "http://api.flickr.com/services/feeds/groups_pool.gne?id=2327386@N22&lang=en-us&format=atom" -o qgisflickrscreenshots.atom

# make backup
mv qgisplanet.atom qgisplanet.atom.0
# get latest planet feed
curl -o qgisplanet.atom "http://planet.qgis.org/planet/feed/atom/"

# change logs
# for 2.4
mv visualchangelog24.atom visualchangelog24.atom.0
curl "http://changelog.linfiniti.com/qgis/version/2.4.0/atom" -o visualchangelog24.atom
# for 2.2
mv visualchangelog22.atom visualchangelog22.atom.0
curl "http://changelog.linfiniti.com/qgis/version/21/atom" -o visualchangelog22.atom
# for 2.0
mv visualchangelog20.atom visualchangelog20.atom.0
curl "http://changelog.linfiniti.com/qgis/version/200/atom" -o visualchangelog20.atom

# qugsnews
mv qugsnews.atom qugsnews.atom.0
curl https://raw.githubusercontent.com/qgis/QGIS-Website/master/source/feeds/qugsnews.atom -o qugsnews.atom
