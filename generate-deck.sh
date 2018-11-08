#!/bin/bash

wget https://duolingo-mandarin-chinese.netlify.com

cat index.html | sed -e "s/<table/\n<table/g" | sed -e "s/<tr/\n<tr/g" | grep "<tr><td>" | sed -e "s/<tr><td>//g" | sed -e "s/<\/td><td>/\t/g" | sed -e "s/<\/td.*//g" > words.tsv

rm -f index.html
