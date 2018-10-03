#!/bin/bash
#Program to print n fibonacci numbers
n=$1
i=1
a=0
b=1
echo -n "$a $b "
while [ $i -lt $((n-1)) ]
do
	temp=$b
	b=$((b+a))
	a=$temp
	echo -n "$b "
	i=$((i+1))
done
echo

