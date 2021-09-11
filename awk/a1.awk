BEGIN{
#	print "begin block";
	FS=" ";	
	n=0;
	sum1=0;
	sum2=0;
}
{
#	print "code block";
	print $1, $2;
	n++;
	sum1+=$1;
	sum2+=$2;
#	if ( $1 ~ /10/)
#	{
#		print "100";
#		print "ok";
#	}
}
END{
#	print "end block"
#	print n;
	print sum1, sum2;

}
