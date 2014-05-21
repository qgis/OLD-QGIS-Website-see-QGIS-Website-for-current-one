
# only languages which have translations in transifex
for LANG in en ca de es fa fi fr id it ja km_KH ko nl pl pt_BR pt_PT ro tr ru uk zh_CN
  do
    /bin/bash ./docker-run.sh full LANG=$LANG
    rsync -hvrz -e ssh --progress output/html/$LANG qgis.osgeo.osuosl.org:/var/www/qgis_new_web2/QGIS-Website/live/html
  done
