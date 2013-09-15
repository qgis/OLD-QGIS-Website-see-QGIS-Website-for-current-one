#!/bin/bash
#

# to be run from the root directory
# scripts/pulldocsources.sh

QGIS_DOC_DIR='QGIS-Documentation'
QGIS_DOC_BRANCH='master'
LANGUAGES='en de'

if [ $1 ]; then
  LANGUAGES="$@"
fi

echo $LANGUAGES

cd ./ext

# if there is NOT a QGIS-Documentation directory
if [ ! -d $QGIS_DOC_DIR ]; then
    git clone https://github.com/qgis/QGIS-Documentation.git $QGIS_DOC_DIR
fi

# checkout the branch we want to incorporate into the documentation
cd $QGIS_DOC_DIR
git checkout $QGIS_DOC_BRANCH
# pull latest
git pull

cd ../..
# copy documentation conf.py as docs_conf.py into the sources dir
cp ext/$QGIS_DOC_DIR/source/conf.py source/docs_conf.py


for LANG in ${LANGUAGES}
do
    # copy sources of documentation into website source tree
    echo "Copying sources for '${LANG}' into website source tree"
    cp -r ext/$QGIS_DOC_DIR/source/docs/* source/docs
    echo "Copying resources/images and translations for '${LANG}' into website source tree"
    cp -r ext/$QGIS_DOC_DIR/resources/${LANG}/* resources/${LANG}
    cp -r ext/$QGIS_DOC_DIR/i18n/${LANG}/LC_MESSAGES/docs i18n/${LANG}/LC_MESSAGES
done
