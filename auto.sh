#!/bin/bash
for ((i=1; i<=10; i++))
do
	python3 autoCreate.py $1
	python autoSend.py ./
	echo $i
	sleep 2
done
