FROM mrussorb/cluster-base:debian_buster
LABEL maintainer="MarcusRB <marcusrb@dataschool.tech>"


# -- Layer: Image Metadata

ARG build_date

LABEL org.label-schema.build-date=${build_date}
LABEL org.label-schema.name="Final Project data architecture on Docker - Spark-Hive base Image"
LABEL org.label-schema.description="Spark-Hive image"
LABEL org.label-schema.url="https://github.com/marcusRB/final-project-cluster-on-docker"
LABEL org.label-schema.schema-version="1.0"

# # Install sbt
# RUN apt-get update
# RUN apt-get -y install openjdk-8-jdk
# ENV SBT_VERSION 1.5.0
# RUN wget http://dl.bintray.com/sbt/debian/sbt-${SBT_VERSION}.deb -O /tmp/sbt.deb && \
#     dpkg -i /tmp/sbt.deb && \
#     rm -f /tmp/sbt.deb

# Install Hadoop
ENV HADOOP_HOME /usr/bin/hadoop-${hadoop_version}
ENV HADOOP_CONF_DIR=$HADOOP_HOME/conf
ENV PATH $PATH:$HADOOP_HOME/bin
RUN curl https://archive.apache.org/dist/hadoop/common/hadoop-${hadoop_version}/hadoop-${hadoop_version}.tar.gz -o hadoop.tgz && \
    tar -xf hadoop.tgz && \
    mv hadoop-${hadoop_version} /usr/bin/ \
  && rm -rf $HADOOP_HOME/share/doc \
  && chown -R root:root $HADOOP_HOME \
  && mkdir -p $HADOOP_HOME/logs \
  && mkdir -p $HADOOP_CONF_DIR \
  && chmod 777 $HADOOP_CONF_DIR \
  && chmod 777 $HADOOP_HOME/logs \
  && rm hadoop.tgz


# Install Hive
ARG hive_version
ENV HIVE_HOME=/usr/bin/apache-hive-${hive_version}-bin
ENV HIVE_CONF_DIR=$HIVE_HOME/conf
ENV PATH $PATH:$HIVE_HOME/bin
RUN curl https://archive.apache.org/dist/hive/hive-${hive_version}/apache-hive-${hive_version}-bin.tar.gz -o hive.tgz && \
    tar -xf hive.tgz && \
    mv apache-hive-${hive_version}-bin /usr/bin/ \
  && chown -R root:root $HIVE_HOME \
  && mkdir -p $HIVE_HOME/hcatalog/var/log \
  && mkdir -p $HIVE_HOME/var/log \
  && mkdir -p /data/hive/ \
  && mkdir -p $HIVE_CONF_DIR \
  && chmod 777 $HIVE_HOME/hcatalog/var/log \
  && chmod 777 $HIVE_HOME/var/log \
  && rm hive.tgz

RUN ln -s $HADOOP_HOME/share/hadoop/tools/lib/aws-java-sdk-1.7.4.jar $HIVE_HOME/lib/. 
RUN ln -s $HADOOP_HOME/share/hadoop/tools/lib/hadoop-aws-2.7.3.jar $HIVE_HOME/lib/. 

# Install Spark

ARG spark_version
ARG hadoop_version
RUN curl https://archive.apache.org/dist/spark/spark-${spark_version}/spark-${spark_version}-bin-hadoop${hadoop_version}.tgz -o spark.tgz && \
    tar -xf spark.tgz && \
    mv spark-${spark_version}-bin-hadoop${hadoop_version} /usr/bin/ && \
    echo "alias pyspark=/usr/bin/spark-${spark_version}-bin-hadoop${hadoop_version}/bin/pyspark" >> ~/.bashrc && \
    echo "alias spark-shell=/usr/bin/spark-${spark_version}-bin-hadoop${hadoop_version}/bin/spark-shell" >> ~/.bashrc && \
    mkdir /usr/bin/spark-${spark_version}-bin-hadoop${hadoop_version}/logs && \
    rm spark.tgz

ENV SPARK_HOME /usr/bin/spark-${spark_version}-bin-hadoop${hadoop_version}
ENV SPARK_CONF_DIR=$SPARK_HOME/conf
ENV SPARK_MASTER_HOST spark-master
ENV SPARK_MASTER_PORT 7077
ENV PYSPARK_PYTHON python3

# Install Readline Wrapper
RUN apt-get update && apt-get install -y rlwrap \
 && rm -rf /var/lib/apt/lists/*

RUN ln -s $HADOOP_HOME/share/hadoop/tools/lib/aws-java-sdk-1.7.4.jar $SPARK_HOME/jars/. 
RUN ln -s $HADOOP_HOME/share/hadoop/tools/lib/hadoop-aws-2.7.3.jar $SPARK_HOME/jars/. 


# Configure
ADD docker/spark-hive-base/files/hive-site.xml $HIVE_CONF_DIR/
ADD docker/spark-hive-base/files/hive-site.xml $SPARK_CONF_DIR/
ADD docker/spark-hive-base/files/start.sh /
ADD docker/spark-hive-base/files/init.sh /
ADD docker/spark-hive-base/files/beeline.sh /

# EXPOSE 22
EXPOSE 4040
EXPOSE 9083
EXPOSE 10000


# -- Runtime

WORKDIR ${SPARK_HOME}
ENTRYPOINT ["/beeline.sh"]