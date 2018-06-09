#!/bin/bash

# cd to script dir
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR

now=`date`
echo "Starting: $now"

if [ -f running ]; then
	echo "$0 still running"
	exit 1
fi

touch running
trap "rm $PWD/running" EXIT

TARGET=${1:-full}

# throw away building artefacts
git stash
git stash drop
# get latest version
git pull

# only languages which have translations in transifex
: ${langs:=en ca da de es fa fi fr gl hu id it ja km_KH ko lt nl pl pt_BR pt_PT ro tr ru uk zh_CN zh_TW}

# if you only want to build one language, do:
# $ langs=de ./docker-world.sh

for l in $langs
  do
    time /bin/bash ./docker-run.sh $TARGET LANG=$l
    #time rsync -hvrzc -e ssh --progress output/html/$l qgis.osgeo.osuosl.org:/var/www/qgisdata/QGIS-Website/live/html
    # 1 dec 2017: sync to qgis2
    time rsync -hvrzc --progress output/html/$l /var/www/qgisdata/QGIS-Website/live/html
  done

time rsync -hvzc -e ssh --progress output/html/version.txt /var/www/qgisdata/QGIS-Website/live/html

now=`date`
echo "Finished: $now"
