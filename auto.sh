#!/bin/bash
for ((i=1; i<=10; i++))
do
	python3 autoCreate.py $1
	python autoSend.py $2
	echo $i
	sleep 3
done
