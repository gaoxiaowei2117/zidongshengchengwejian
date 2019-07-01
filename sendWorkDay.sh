#!/bin/bash
WORK_PATH="/home/volume/zidongshengchengwejian"
LOG_FILE="/tmp/zidongshengchengwenjian.log"
time=`date "+%Y-%m-%d %H:%M:%S "`
echo "${time}" > $LOG_FILE

cd $WORK_PATH
./auto.sh ./changhe/shimoban/ ./changhe/1 >> $LOG_FILE
./auto.sh ./haitang/ ./haitang/1 >> $LOG_FILE
