#!/bin/bash

apppath="/c/users/sgce/ced"
configpath="/c/users/sgce/ced/config"
environment="$1"
srcpath=`pwd`

cd $srcpath/sgce
git checkout $environment
git pull

rsync -avz --no-g --delete-after . $apppath --exclude=support --exclude=README.md --exclude=.git --exclude=.gitignore --exclude=AlterForProduction.txt --exclude=requirements.txt

cd $srcpath/sgceconfig
git checkout $environment
git pull

rsync -avz --no-g --delete-after . $configpath --exclude=.git --exclude=.gitignore

cd /c/Users/sgce/ced

ls
python -m compileall .
python manage.py check
date
