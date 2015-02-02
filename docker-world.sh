#!/bin/bash

now=`date`
echo "Starting $now"

if [ -f running ]; then
	echo "$0 still running"
	exit 1
fi

touch running
trap "rm $PWD/running" EXIT

TARGET=${1:-full}

# cd to script dir
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR
# throw away building artefacts
git stash
git stash drop
# get latest version
git pull

# only languages which have translations in transifex
: ${langs:=en ca da de es fa fi fr id it ja km_KH ko nl pl pt_BR pt_PT ro tr ru uk zh_CN}

# if you only want to build one language, do:
# $ langs=de ./docker-world.sh

for l in $langs
  do
    time /bin/bash ./docker-run.sh $TARGET LANG=$l
    time rsync -hvrzc -e ssh --progress output/html/$l qgis.osgeo.osuosl.org:/var/www/qgisdata/QGIS-Website/live/html
  done
