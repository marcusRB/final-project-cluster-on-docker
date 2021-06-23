#!/bin/bash
#
# -- Build Apache Spark Standalone Cluster Docker Images
# Versión 1.2.0 - 2021-06-19
# add requirements.txt
# add MLflow
# remove Hive image
# fixed docker build tags
# ----------------------------------------------------------------------------------------------------------------------
# -- Variables ---------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

BUILD_VERSION="v1.2.0"
BUILD_DATE="$(date -u +'%Y-%m-%d')"

SHOULD_BUILD_BASE="$(grep -m 1 build_base build.yml | grep -o -P '(?<=").*(?=")')"
SHOULD_BUILD_SPARK="$(grep -m 1 build_spark build.yml | grep -o -P '(?<=").*(?=")')"
SHOULD_BUILD_JUPYTERLAB="$(grep -m 1 build_jupyter build.yml | grep -o -P '(?<=").*(?=")')"

SPARK_VERSION="$(grep -m 1 spark build.yml | grep -o -P '(?<=").*(?=")')"
JUPYTERLAB_VERSION="$(grep -m 1 jupyterlab build.yml | grep -o -P '(?<=").*(?=")')"

SPARK_VERSION_MAJOR=${SPARK_VERSION:0:1}

if [[ "${SPARK_VERSION_MAJOR}" == "2" ]]
then
  HADOOP_VERSION="2.7"
  SCALA_VERSION="2.11.12"
  SCALA_KERNEL_VERSION="0.6.0"
  HIVE_VERSION="2.3.8"
elif [[ "${SPARK_VERSION_MAJOR}"  == "3" ]]
then
  HADOOP_VERSION="3.2"
  SCALA_VERSION="2.12.10"
  SCALA_KERNEL_VERSION="0.10.9"
  HIVE_VERSION="3.1.2"
  POSTGRESQL_VERSION="42.2.19"
else
  exit 1
fi

# ----------------------------------------------------------------------------------------------------------------------
# -- Functions----------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

function cleanContainers() {

    container="$(docker ps -a | grep 'mrussorb/cluster-jupyterlab:${JUPYTERLAB_VERSION}-spark${SPARK_VERSION}-${BUILD_VERSION}' | awk '{print $1}')"
    docker stop "${container}"
    docker rm "${container}"

    container="$(docker ps -a | grep 'mrussorb/cluster-spark-worker:${SPARK_VERSION}-hadoop${HADOOP_VERSION}-${BUILD_VERSION}' -m 1 | awk '{print $1}')"
    while [ -n "${container}" ];
    do
      docker stop "${container}"
      docker rm "${container}"
      container="$(docker ps -a | grep 'mrussorb/cluster-spark-worker:${SPARK_VERSION}-hadoop${HADOOP_VERSION}-${BUILD_VERSION}' -m 1 | awk '{print $1}')"
    done

    container="$(docker ps -a | grep 'mrussorb/cluster-spark-master:${SPARK_VERSION}-hadoop${HADOOP_VERSION}-${BUILD_VERSION}' | awk '{print $1}')"
    docker stop "${container}"
    docker rm "${container}"

    container="$(docker ps -a | grep 'mrussorb/cluster-spark-base:${SPARK_VERSION}-hadoop${HADOOP_VERSION}-${BUILD_VERSION}' | awk '{print $1}')"
    docker stop "${container}"
    docker rm "${container}"

    container="$(docker ps -a | grep 'base' | awk '{print $1}')"
    docker stop "${container}"
    docker rm "${container}"

}

function cleanImages() {

    if [[ "${SHOULD_BUILD_JUPYTERLAB}" == "true" ]]
    then
      docker rmi -f "$(docker images | grep -m 1 'mrussorb/cluster-jupyterlab:${JUPYTERLAB_VERSION}-spark${SPARK_VERSION}-${BUILD_VERSION}' | awk '{print $3}')"
    fi

    if [[ "${SHOULD_BUILD_SPARK}" == "true" ]]
    then
      docker rmi -f "$(docker images | grep -m 1 'mrussorb/cluster-spark-worker:${SPARK_VERSION}-hadoop${HADOOP_VERSION}-${BUILD_VERSION}' | awk '{print $3}')"
      docker rmi -f "$(docker images | grep -m 1 'mrussorb/cluster-spark-master:${SPARK_VERSION}-hadoop${HADOOP_VERSION}-${BUILD_VERSION}' | awk '{print $3}')"
      docker rmi -f "$(docker images | grep -m 1 'mrussorb/cluster-spark-base:${SPARK_VERSION}-hadoop${HADOOP_VERSION}-${BUILD_VERSION}' | awk '{print $3}')"
    fi

    if [[ "${SHOULD_BUILD_BASE}" == "true" ]]
    then
      docker rmi -f "$(docker images | grep -m 1 'mrussorb/cluster-base:debian_buster-${BUILD_VERSION}' | awk '{print $3}')"
    fi

}

function cleanVolume() {
  docker volume rm "hadoop-distributed-file-system"
}

function buildImages() {

  if [[ "${SHOULD_BUILD_BASE}" == "true" ]]
  then
    docker build \
      --build-arg build_date="${BUILD_DATE}" \
      --build-arg scala_version="${SCALA_VERSION}" \
      --build-arg build_version="${BUILD_VERSION}" \
      -f docker/base/Dockerfile \
      -t mrussorb/cluster-base:debian_buster-${BUILD_VERSION} .
  fi

  if [[ "${SHOULD_BUILD_SPARK}" == "true" ]]
  then

    docker build \
      --build-arg build_date="${BUILD_DATE}" \
      --build-arg spark_version="${SPARK_VERSION}" \
      --build-arg hadoop_version="${HADOOP_VERSION}" \
      --build-arg postgres_version="${POSTGRESQL_VERSION}" \
      --build-arg build_version="${BUILD_VERSION}" \
      -f docker/spark-base/Dockerfile \
      -t mrussorb/cluster-spark-base:${SPARK_VERSION}-hadoop${HADOOP_VERSION}-${BUILD_VERSION} .

    docker build \
      --build-arg build_date="${BUILD_DATE}" \
      --build-arg spark_version="${SPARK_VERSION}" \
      --build-arg hadoop_version="${HADOOP_VERSION}" \
      --build-arg build_version="${BUILD_VERSION}" \
      -f docker/spark-master/Dockerfile \
      -t mrussorb/cluster-spark-master:${SPARK_VERSION}-hadoop${HADOOP_VERSION}-${BUILD_VERSION} .

    docker build \
      --build-arg build_date="${BUILD_DATE}" \
      --build-arg spark_version="${SPARK_VERSION}" \
      --build-arg hadoop_version="${HADOOP_VERSION}" \
      --build-arg build_version="${BUILD_VERSION}" \
      -f docker/spark-worker/Dockerfile \
      -t mrussorb/cluster-spark-worker:${SPARK_VERSION}-hadoop${HADOOP_VERSION}-${BUILD_VERSION} .

  fi

  if [[ "${SHOULD_BUILD_JUPYTERLAB}" == "true" ]]
  then
    docker build \
      --build-arg build_date="${BUILD_DATE}" \
      --build-arg scala_version="${SCALA_VERSION}" \
      --build-arg spark_version="${SPARK_VERSION}" \
      --build-arg jupyterlab_version="${JUPYTERLAB_VERSION}" \
      --build-arg scala_kernel_version="${SCALA_KERNEL_VERSION}" \
      --build-arg build_version="${BUILD_VERSION}" \
      -f docker/jupyterlab/Dockerfile \
      -t mrussorb/cluster-jupyterlab:${JUPYTERLAB_VERSION}-spark${SPARK_VERSION}-${BUILD_VERSION} .
  fi

}

# ----------------------------------------------------------------------------------------------------------------------
# -- Main --------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

cleanContainers;
cleanImages;
cleanVolume;
buildImages;
