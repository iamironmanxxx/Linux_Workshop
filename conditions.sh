#!/bin/bash
a=10
b=20
c=30

if [ $a -gt $b ]
then
	echo "$a is greater than $b"
else
	echo "$b is greater than $a"
fi

if [ $a -gt $b -o $a -gt $c ]
then
	echo "$a is not the smallest no"
fi

