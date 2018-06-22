#!/usr/bin/env bash

# set scripts dir as cwd
#cd "${0%/*}"

if [ -f running ]; then
    echo "$0 still running"
    exit 1
fi
touch running

git pull --rebase

echo $1 | perl scripts/adddonor.pl

git commit -a -m "Donor $1 (via Stripe) added"

git push origin master

rm running
exit 0

