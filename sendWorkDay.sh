#!/bin/bash
WORK_PATH="/home/volume/zidongshengchengwejian"
LOG_FILE="/tmp/zidongshengchengwenjian_workday.log"
time=`date "+%Y-%m-%d %H:%M:%S "`
echo "${time}" > $LOG_FILE

cd $WORK_PATH
./auto_trans.sh ./changhe/jisuban/ ./changhe/1 10 >> $LOG_FILE
./auto_trans.sh ./haitang/ ./haitang/1 20 >> $LOG_FILE
./auto_trans.sh ./kangda/chujiaquan/ ./kangda/chujiaquan/1 10 >> $LOG_FILE
./auto_trans.sh ./kangda/jiaquanjiance/ ./kangda/jiaquanjiance/2 10 >> $LOG_FILE
./auto_trans.sh ./yishang/ yishang/1/ 10 >> $LOG_FILE
./auto_trans.sh ./aishangjia/ ./aishangjia/1 20 >> $LOG_FILE
#./auto.sh ./woke/ woke/1/ >> $LOG_FILE
