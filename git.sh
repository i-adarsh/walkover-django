#!/usr/bin/bash

git add .
git rm -r --cached ./env
git commit -m "Final"
git push --set-upstream origin main