FROM mrussorb/cluster-base:debian_buster
LABEL maintainer="MarcusRB <marcusrb@dataschool.tech>"

# -- Layer: Image Metadata

ARG build_date

LABEL org.label-schema.build-date=${build_date}
LABEL org.label-schema.name="Final Project data architecture on Docker - Spark-Base Image"
LABEL org.label-schema.description="Spark-Base image"
LABEL org.label-schema.url="https://github.com/marcusRB/final-project-cluster-on-docker"
LABEL org.label-schema.schema-version="1.0"

# -- Layer: Apache Spark

ARG spark_version
ARG hadoop_version
ARG postgres_version

RUN curl https://archive.apache.org/dist/spark/spark-${spark_version}/spark-${spark_version}-bin-hadoop${hadoop_version}.tgz -o spark.tgz && \
    tar -xf spark.tgz && \
    mv spark-${spark_version}-bin-hadoop${hadoop_version} /usr/bin/ && \
    echo "alias pyspark=/usr/bin/spark-${spark_version}-bin-hadoop${hadoop_version}/bin/pyspark" >> ~/.bashrc && \
    echo "alias spark-shell=/usr/bin/spark-${spark_version}-bin-hadoop${hadoop_version}/bin/spark-shell" >> ~/.bashrc && \
    mkdir /usr/bin/spark-${spark_version}-bin-hadoop${hadoop_version}/logs && \
    rm spark.tgz

ENV SPARK_HOME /usr/bin/spark-${spark_version}-bin-hadoop${hadoop_version}
ENV SPARK_MASTER_HOST spark-master
ENV SPARK_MASTER_PORT 7077
ENV PYSPARK_PYTHON python3

# -- Drivers --
RUN curl https://jdbc.postgresql.org/download/postgresql-${postgres_version}.jar -o  postgresql-${postgres_version}.jar && \ 
    mv postgresql-${postgres_version}.jar ${SPARK_HOME}/jars

RUN curl https://repos.spark-packages.org/maropu/spark-sql-server/0.1.7-spark2.4/spark-sql-server-0.1.7-spark2.4.jar -o spark-sql-server-0.1.7-spark2.4.jar && \
    mv spark-sql-server-0.1.7-spark2.4.jar ${SPARK_HOME}/jars

RUN curl https://repos.spark-packages.org/dibbhatt/kafka-spark-consumer/2.1.0/kafka-spark-consumer-2.1.0.jar -o kafka-spark-consumer-2.1.0.jar && \
    mv kafka-spark-consumer-2.1.0.jar ${SPARK_HOME}/jars

RUN curl https://repo1.maven.org/maven2/org/mongodb/spark/mongo-spark-connector_2.12/3.0.1/mongo-spark-connector_2.12-3.0.1.jar -o mongo-spark-connector_2.12-3.0.1.jar && \
    mv mongo-spark-connector_2.12-3.0.1.jar ${SPARK_HOME}/jars

RUN curl https://repo1.maven.org/maven2/io/delta/delta-core_2.12/1.0.0/delta-core_2.12-1.0.0.jar -o delta-core_2.12-1.0.0.jar && \
    mv delta-core_2.12-1.0.0.jar ${SPARK_HOME}/jars

# -- Runtime

WORKDIR ${SPARK_HOME}