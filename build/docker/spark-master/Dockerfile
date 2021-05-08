ARG spark_version
FROM spark-base:${spark_version}
LABEL maintainer="MarcusRB <marcusrb@dataschool.tech>"

# -- Layer: Image Metadata

ARG build_date

LABEL org.label-schema.build-date=${build_date}
LABEL org.label-schema.name="Final Project data architecture on Docker - Spark-Master Image"
LABEL org.label-schema.description="Spark-Master image"
LABEL org.label-schema.url="https://github.com/marcusRB/final-project-cluster-on-docker"
LABEL org.label-schema.schema-version="1.0"

# -- Runtime

EXPOSE 8080 7077 10000

CMD bin/spark-class org.apache.spark.deploy.master.Master >> logs/spark-master.out