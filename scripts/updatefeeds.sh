
# script to be run on server serving the static content of the website
# doc root in /ar/www/qgis_new_web/QGIS-Website/live/html

mkdir -p /var/www/qgisdata/QGIS-Website/live/html/feeds
# cd to feed output dir
cd /var/www/qgisdata/QGIS-Website/live/html/feeds

# get latest qgis flickrmaps
mv qgisflickrmaps.atom qgisflickrmaps.atom.0
curl "https://api.flickr.com/services/feeds/groups_pool.gne?id=2244553@N22&lang=en-us&format=atom" -o qgisflickrmaps.atom

# get latest qgis flickrscreenshots
mv qgisflickrscreenshots.atom qgisflickrscreenshots.atom.0
curl "https://api.flickr.com/services/feeds/groups_pool.gne?id=2327386@N22&lang=en-us&format=atom" -o qgisflickrscreenshots.atom

# get latest planet feed
mv qgisplanet.atom qgisplanet.atom.0
curl -o qgisplanet.atom "https://plugins.qgis.org/planet/feed/atom/"

# get qugsnews (from github)
mv qugsnews.atom qugsnews.atom.0
curl https://raw.githubusercontent.com/qgis/QGIS-Website/master/source/feeds/qugsnews.atom -o qugsnews.atom

# get sponsors (from changelog.qgis.org/projecta)
mv members.json members.json.0
# 20211029 TEMPORARILY use -k == no cert fix !!! PLEASE REMOVE/FIX WHEN POSSIBLE
curl -k -A Mozilla https://changelog.qgis.org/en/qgis/members/json/ -o members.json
# and list of past sponsors too
mv qgispastmembers.json qgispastmembers.json.0
# 20211029 TEMPORARILY use -k == no cert fix !!! PLEASE REMOVE/FIX WHEN POSSIBLE
curl -k -A Mozilla https://changelog.qgis.org/en/qgis/past-members/json/?years_limit=2 -o qgispastmembers.json

# 20220317 rsync feeds to new server
rsync -hvzc -e ssh --progress /var/www/qgisdata/QGIS-Website/live/html/feeds/* root@195.201.96.242:/var/www/qgisdata/QGIS-Website/live/html/feeds/
