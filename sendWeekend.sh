#!/bin/bash
WORK_PATH="/home/volume/zidongshengchengwejian"
LOG_FILE="/tmp/zidongshengchengwenjian_weekend.log"
time=`date "+%Y-%m-%d %H:%M:%S "`
echo "${time}" > $LOG_FILE

cd $WORK_PATH

./auto_trans.sh ./changhe/jisuban/ ./changhe/2 >> $LOG_FILE
./auto_trans.sh ./yinuo/caigangban/ ./yinuo/1 >> $LOG_FILE
./auto_trans.sh ./yinuo/caigangban/ ./yinuo/2 >> $LOG_FILE
./auto_trans.sh ./kangda/chujiaquan/ ./kangda/chujiaquan/1 >> $LOG_FILE
./auto_trans.sh aishangjia/ aishangjia/1 >> $LOG_FILE
