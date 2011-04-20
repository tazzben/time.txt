#!/bin/bash
find . -name "*.pyc" -exec rm '{}' ';'
rm dist/time.zip
rm dist/time.tar.gz
mv src time
tar -pczf dist/time.tar.gz   --exclude=".*" --exclude="/.*" --exclude="/*/.*" --exclude="*.pyc" ./time
mv time/time time/time.py
zip -r dist/time.zip time/[!\.]* -x \*/\.*
mv time/time.py time/time
mv time src