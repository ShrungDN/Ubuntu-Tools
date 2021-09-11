#!/usr/bin/bash

# list all shell scripts in /bin 

touch list_of_scripts.txt
echo " " > list_of_scripts.txt
for n in `ls -1 /bin`
do
	file /bin/$n | egrep "script" | awk 'BEGIN{FS=":"}{print $1;}END{}' >> list_of_scripts.txt 
done

# to see if these script files have a function definition

for n in `cat list_of_scripts.txt`
do
	echo $n 
	cat $n | egrep "\(\)" #grep "()" has same meaning as () doesnt meant anything special to grep
			      #but for egrep, () has special meaning so use \ to use it as normal brackets	
	echo "--------------------------------------------------"
done
