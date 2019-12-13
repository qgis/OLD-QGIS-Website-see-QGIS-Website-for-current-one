# to be able to run the full image (including pulling from transifex)
# you need a valid .transifexrc file with your credentials in your home dir
# this one is temporarily copied to the project dir
# and removed after build
# maybe better to create a qgisdocker transifex user?

cp ~/.transifexrc .
pwd=$(pwd)
docker run -v $pwd:/site -w="/site" --rm=true --name="qgis_website_build" qgis/sphinx_html_3:latest make $@;build_result=$?
rm -rf .transifexrc
echo $build_result
exit $build_result
