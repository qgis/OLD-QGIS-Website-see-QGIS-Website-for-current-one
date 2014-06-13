
# only languages which have translations in transifex
: ${langs:=en ca de es fa fi fr id it ja km_KH ko nl pl pt_BR pt_PT ro tr ru uk zh_CN}

# if you only want to build one language, do:
# $ langs=de ./docker-world.sh

#for LANG in en ca de es fa fi fr id it ja km_KH ko nl pl pt_BR pt_PT ro tr ru uk zh_CN
for l in $langs
  do
    /bin/bash ./docker-run.sh full LANG=$l
    rsync -hvrz -e ssh --progress output/html/$l qgis.osgeo.osuosl.org:/var/www/qgisdata/QGIS-Website/live/html
  done
