#!/bin/bash
for ((i=1; i<=3; i++))
do
	python3 autoCreate.py $1
	python autoSend.py $2
	echo $i
	sleep 20
done
