#!/bin/bash
#
# -- Build Apache Spark Standalone Cluster Docker Images

# ----------------------------------------------------------------------------------------------------------------------
# -- Variables ---------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

BUILD_DATE="$(date -u +'%Y-%m-%d')"

SHOULD_BUILD_SPARK_HIVE="$(grep -m 1 build_spark_hive build.yml | grep -o -P '(?<=").*(?=")')"
SPARK_VERSION="$(grep -m 1 spark build.yml | grep -o -P '(?<=").*(?=")')"


SPARK_VERSION_MAJOR=${SPARK_VERSION:0:1}

if [[ "${SPARK_VERSION_MAJOR}" == "2" ]]
then
  HADOOP_VERSION="2.7"
  SCALA_VERSION="2.11.12"
  SCALA_KERNEL_VERSION="0.6.0"
  HIVE_VERSION="2.3.8"
elif [[ "${SPARK_VERSION_MAJOR}"  == "3" ]]
then
  HADOOP_VERSION="3.2.0"
  SCALA_VERSION="2.12.10"
  SCALA_KERNEL_VERSION="0.10.9"
  HIVE_VERSION="3.1.2"
else
  exit 1
fi

# ----------------------------------------------------------------------------------------------------------------------
# -- Functions----------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

function cleanContainers() {

    container="$(docker ps -a | grep 'spark-hive-worker' -m 1 | awk '{print $1}')"
    while [ -n "${container}" ];
    do
      docker stop "${container}"
      docker rm "${container}"
      container="$(docker ps -a | grep 'spark-hive-worker' -m 1 | awk '{print $1}')"
    done

    container="$(docker ps -a | grep 'spark-hive-master' | awk '{print $1}')"
    docker stop "${container}"
    docker rm "${container}"



}

function cleanImages() {


    if [[ "${SHOULD_BUILD_SPARK_HIVE}" == "true" ]]
    then
      docker rmi -f "$(docker images | grep -m 1 'spark-hive-worker' | awk '{print $3}')"
      docker rmi -f "$(docker images | grep -m 1 'spark-hive-master' | awk '{print $3}')"
    fi
}

function cleanVolume() {
  docker volume rm "hadoop-distributed-file-system"
}

function buildImages() {

  if [[ "${SHOULD_BUILD_SPARK_HIVE}" == "true" ]]
  then

    docker build \
      --build-arg build_date="${BUILD_DATE}" \
      --build-arg spark_version="${SPARK_VERSION}" \
      --build-arg hadoop_version="${HADOOP_VERSION}" \
      --build-arg hive_version="${HIVE_VERSION}" \
      -f docker/spark-hive-master/Dockerfile \
      -t spark-hive-master:${SPARK_VERSION}-hive${HIVE_VERSION} .

    docker build \
      --build-arg build_date="${BUILD_DATE}" \
      --build-arg spark_version="${SPARK_VERSION}" \
      --build-arg hadoop_version="${HADOOP_VERSION}" \
      --build-arg hive_version="${HIVE_VERSION}" \
      -f docker/spark-hive-worker/Dockerfile \
      -t spark-hive-worker:${SPARK_VERSION}-hive${HIVE_VERSION} .

  fi

}

# ----------------------------------------------------------------------------------------------------------------------
# -- Main --------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

cleanContainers;
cleanImages;
cleanVolume;
buildImages;
