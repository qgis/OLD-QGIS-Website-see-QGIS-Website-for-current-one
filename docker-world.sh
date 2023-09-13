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
: ${langs:=en ca da de es fa fi fr gl hu id it ja km_KH ko lt nl pl pt_BR pt_PT ro tr ru uk zh-Hans zh-Hant}

# if you only want to build one language, do:
# $ langs=de ./docker-world.sh

for l in $langs
  do
    ./docker-run.sh $TARGET LANG=$l
    build_ok=$?
    if [[ "$build_ok" = "0" ]]; then
      echo "Build OK: syncing to web"
      # 20220317: sync to www2.qgis.org
      time rsync -hvrzc --delete --progress output/html/$l www2.qgis.org:/var/www/qgisdata/QGIS-Website/live/html
    else
      echo "Build FAILED: not syncing to web";
    fi
  done

# 20220317: sync to www2.qgis.org
time rsync -hvzc -e ssh --progress output/html/version.txt output/html/version-ltr.txt output/html/version.json source/schedule.ics www2.qgis.org:/var/www/qgisdata/QGIS-Website/live/html

now=`date`
echo "Finished: $now"
