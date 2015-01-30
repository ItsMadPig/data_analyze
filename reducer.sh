#!/bin/bash

awk '
BEGIN{
	FS="\t";
	OFS="\t";
	prev="";
	count=0;
}
{
	#printf("name:%s\tcount:%i\n",$name,count);
	#print($1,$2);
	if (prev!=$1 && prev!=""){
		print(prev,count);
		count=$2;
	}else{
		count+=$2;
	}
	prev=$1
}
END {
	print(prev,count)
}
'