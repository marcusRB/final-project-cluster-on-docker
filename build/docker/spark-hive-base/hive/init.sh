#!/bin/bash

# Get Spark Master stuff
echo export SPARK_MASTER_IP=`hostname -i` >> $HOME/.bashrc
echo export SPARK_MASTER_HOST=`hostname` >> $HOME/.bashrc
echo export SPARK_LOCAL_IP=`hostname -i` >> $HOME/.bashrc
source $HOME/.bashrc

# /etc/init.d/ssh start
if [ ! -d "/shared_data/hive/metastore_db" ]; then
  echo "Setting up metastore"
  cd /data/hive
  ${HIVE_HOME}/bin/schematool -dbType mysql -initSchema 
  cd
fi
${HIVE_HOME}/hcatalog/sbin/hcat_server.sh start 
${SPARK_HOME}/sbin/start-master.sh -h ${SPARK_MASTER_HOST} -p 4040
${SPARK_HOME}/sbin/start-slave.sh spark://${SPARK_MASTER_HOST}:4040 -p 4041
${SPARK_HOME}/sbin/start-thriftserver.sh --master "spark://${SPARK_MASTER_HOST}:4040" --driver-memory 1G --executor-memory 1G --total-executor-cores 2 --executor-cores 1 --conf "spark.sql.shuffle.partitions=4" 
${LIVY_HOME}/bin/livy-server start & tail -f /dev/null #stay live as live-server exits