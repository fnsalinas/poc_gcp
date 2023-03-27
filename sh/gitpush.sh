#!/bin/bash

cd $APP_MAIN_PATH;


read -p "Enter commit message: " msg;
actualdatetime=$(date '+%Y-%m-%d %H:%M:%S');

git status;
git add .;
git commit -m "$msg $actualdatetime";
git push;
