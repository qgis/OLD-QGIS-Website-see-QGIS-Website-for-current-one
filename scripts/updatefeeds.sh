
# update planet first
/home/web/qgis-django/update_planet.sh

# cd to feed output dir
cd /var/www/qgis_new_web/QGIS-Website/live/html/feeds

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
