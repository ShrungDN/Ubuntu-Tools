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


# function  to print fibonacci numbers below $1 

fib() {

	n1=1; #this is mostly global variable
	local n2=1;
	echo $n2
	local n=1;

	while [ $n -lt $1 ]	

	do
		echo $n 
		n=`expr $n1 + $n2`
		n2=$n1
		n1=$n
	done
}



echo "";
fib $1;

#echo "XDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD" $n2

echo "now till 1000"
fib 1000; #notice the difference in arguement. the $1 inside function is the arguement given when function is called 
	  #and not the arguement given in command line
echo "";

