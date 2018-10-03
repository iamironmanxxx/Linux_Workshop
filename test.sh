#!/bin/bash
n=$#
prod=1
for x in $@
do
	prod=$((prod*x))
	#echo -n "$prod "
done
echo $prod
echo
prod=1
for((i=1;i<=$n;i++))
do
	num=$i
	prod=$((prod*num))
done
echo $prod
