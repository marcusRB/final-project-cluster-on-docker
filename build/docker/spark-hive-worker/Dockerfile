ARG spark_version
ARG hive_version
FROM spark-hive-base:${spark_version}-hive${hive_version}
LABEL maintainer="MarcusRB <marcusrb@dataschool.tech>"

# -- Layer: Image Metadata

ARG build_date

LABEL org.label-schema.build-date=${build_date}
LABEL org.label-schema.name="Final Project data architecture on Docker - Spark-Hive worker Image"
LABEL org.label-schema.description="Spark-Hive worker image"
LABEL org.label-schema.url="https://github.com/marcusRB/final-project-cluster-on-docker"
LABEL org.label-schema.schema-version="1.0"

# -- Runtime

EXPOSE 8081

CMD bin/spark-class org.apache.spark.deploy.worker.Worker spark://${SPARK_MASTER_HOST}:${SPARK_MASTER_PORT} >> logs/spark-hive-worker.out