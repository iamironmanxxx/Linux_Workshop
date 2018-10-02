#!/bin/bash
blah=(1 2 3 4 5 6 "xyz" "abc")
echo "First for loop"
for var in ${blah[*]}
do
	echo $var
done
echo "Second for loop"
for((i=0; i<5;i=i+1))
do
	echo $i #use: echo -n $i to prevent going to newline
done
echo "Third for loop"
for z in {1..10}
do
	echo -n "$z "
done
echo #to go to newline
for z in {1..10..2} #equivalent to z+=2
do
	echo -n "$z "
done
echo
