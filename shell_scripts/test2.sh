#!/usr/bin/bash

# for n in [1,2,3]

date="1 2 3"
date+=" 4"
echo $date
for n in $date
do
	echo $n
done
