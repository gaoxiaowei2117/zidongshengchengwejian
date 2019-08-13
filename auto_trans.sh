#!/bin/bash
echo -e "\033[32m ======================================================================= \033[0m"
for ((i=1; i<=10; i++))
do
	python3 autoCreate_trans.py $1 $2
	#python3 autoSend.py $2
	echo $i
	sleep 3
done
