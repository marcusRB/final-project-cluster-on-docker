#!/bin/bash

DIR="$(cd "$(dirname "$0")" && pwd)"
docker-compose -f $DIR/docker-compose-cluster-spark.kafka.yml up -d