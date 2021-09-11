#!/usr/bin/bash
# if and while loops 

if test $# -eq 0
then	
	echo "provide integer";
# exit 1; is not necessary
	exit 1;
elif test $1 -lt 0;
then 
	echo "provide positive integer"
	exit 1;
else 
	echo "Fibonacci numbers below $1 are"
fi


# while loop to print fibonacci numbers below $1 

n1=1
n2=1
echo $n2
n=1

while [ $n -lt $1 ]	

# or

# while test $n -lt $1

do
	echo $n 
	n=`expr $n1 + $n2`
	n2=$n1
	n1=$n
done
