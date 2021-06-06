ARG spark_version
ARG hadoop_version
FROM cluster-spark-base:${spark_version}-hadoop${hadoop_version}
LABEL maintainer="MarcusRB <marcusrb@dataschool.tech>"

# -- Layer: Image Metadata

ARG build_date

LABEL org.label-schema.build-date=${build_date}
LABEL org.label-schema.name="Final Project data architecture on Docker - Spark-Master Image"
LABEL org.label-schema.description="Spark-Master image"
LABEL org.label-schema.url="https://github.com/marcusRB/final-project-cluster-on-docker"
LABEL org.label-schema.schema-version="1.0"

# -- Environment

ENV SPARK_MASTER_PORT 7077
ENV SPARK_MASTER_WEBUI_PORT 8080
ENV SPARK_MASTER_LOG /spark/logs

EXPOSE 8080 7077 6066

# -- Runtime

CMD bin/spark-class org.apache.spark.deploy.master.Master >> logs/spark-master.out