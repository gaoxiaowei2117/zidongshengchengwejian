#!/bin/bash
WORK_PATH="/home/volume/zidongshengchengwejian"
LOG_FILE="/tmp/zidongshengchengwenjian.log"
time=`date "+%Y-%m-%d %H:%M:%S "`
echo "${time}" > $LOG_FILE

cd $WORK_PATH
./auto.sh ./changhe/shimoban/ ./changhe/1 >> $LOG_FILE
./auto.sh ./haitang/ ./haitang/1 >> $LOG_FILE
./auto.sh ./haitang/ ./haitang/1 >> $LOG_FILE
./auto.sh ./kangda/jiaquanjiance/ ./kangda/jiaquanjiance/2 >> $LOG_FILE
./auto.sh ./yishang/ yishang/1/ >> $LOG_FILE
./auto.sh aishangjia/ aishangjia/1 >> $LOG_FILE
