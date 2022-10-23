#!/bin/bash
function rec_unzip {
tar -xf $1 && rm $1
for i in $(find . -name "*.tar.gz"); do
    if [ -f $i ]
    then
         rec_unzip $i
    fi
done
}
rec_unzip $1
