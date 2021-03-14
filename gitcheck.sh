#!/bin/bash

subfinder -d $1  | httpx > $1.txt

cat '$1.txt'

for item in "$1.txt"
do
  if curl -LI "$item/.git" -o /dev/null -w '%{http_code}\n' -s == 200 -v 
  then 
    curl -LI item -o /dev/null -w '%{http_code}\n' -s >> git.txt    

done  
