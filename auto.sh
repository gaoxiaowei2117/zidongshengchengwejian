#!/bin/bash
for ((i=1; i<=10; i++))
do
	python3 autoCreate.py $1 $2
	#python3 autoSend.py $2
	echo $i
	sleep 3
done
