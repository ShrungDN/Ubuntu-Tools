#!/usr/bin/bash
# script to rename files of type *.jpg to *.JPG

for n in `ls -1 *.JPG`
do
#different methods to do:


#	echo $n
#	cmd="mv $n ${n:0:-3}JPG"
#	eval $cmd 
#	echo $n



#	eval "mv $n ${n:0:-3}JPG"



	mv $n ${n:0:-3}jpg
done 	
