# Final Project - Cluster on Docker 
```
PRO env. Version 1.0.0

```

## Abstract

This final work shows a viable data architecture solution to address the fraud detection use case of the insurance sector, in the same way to see how to analyse the features for the creation of a fraud prediction model. We will proceed with the design of the architecture, analyse the data pipeline in two temporal moments, batch mode and streaming mode, and finally, shows the results. As complement of that, it will be the comparison between different data treatment processes, study the different ways to consider the start-up phase and to detect possible risks. The aim of the work is to be able to combine data architecture, opting for a hybrid method between Lambda and Kappa architecture, in addition using microservices technology based on Docker and machine learning monitoring by MLOps methods and GitHub workflow.

### Architecture Design

- [X] Lambda Architecture
- [X] Kappa Architecture

### Implementation and configuration

- [X] Dockerfile // Docker build

### Microservices

- [X] Spark
- [X] Kafka standalone
- [X] Kafka by Confluent stack
- [X] MongoDB
- [X] PostgreSQL
- [X] NodeJS
- [X] Grafana
- [X] Prometheus
- [ ] R Studio (pending due version conflict server/livy on Spark 3.1.1)
- [X] JupyterLab Notebook
- [ ] Zeppelin (pending due port conflict)
- [X] MLflow
- [ ] Superset (pending)

## Other databases next release

- [ ] HBase (pending)
- [ ] Hive (pending)
- [ ] Cassandra (pending)
- [ ] Druid (pending)

## Jupyter notebooks and code

- [X] Examples on Spark
- [X] Kafka consumer and producer on PySpark
- [X] Porto Seguro's prediction claim on Python
- [X] Porto Seguro's prediction claim on PySpark
- [X] Porto Seguro's prediction claim on Databricks
- [X] Machine Learning MLflow
- [ ] Streaming processin (pending)
- [X] ML codes on Python


## Guide available here

### SETUP Git & Docker Compose

1. Clone master repository

```{bash}
$ git clone https://<repository-url>
```

2. Check Docker-Compose or install

```{bash}
$ apt install docker-compose
```

3. Start main cluster

```{bash}
$ docker-compose -f docker-compose-cluster-spark-kafka.yml up -d
```

4. Check Docker containers

```{bash}
$ docker-compose ps -a
or
$ docker ps -a
```

5. Check Docker logs

```
$ docker-compose -f <docker-compose-file>.yml logs

```

## Start Spark service

1. Start Spark notebook on JupyterLab

<hostname_virtual_machine>.8888

2. Check Spark Master

<hostname_virtual_machine>.8080

3. Check Spark Worker.n

<hostname_virtual_machine>.8081

4. Start JupyterLab notebooks

Upload notebooks

>  from **/workspace/TFM/** directory

5. Check notebooks for theme

- [Porto_Seguros]_PredictionModel_Python_052021_v1_0_0.ipynb

- [Porto_Seguros]_PredictionModel_PySpark_062021_v1_0_0.ipynb

- spark-kafka-consumer.ipynb

- spark-kafka-producer.ipynb


## Start Kafka by Confluent

1. Start Docker-Compose

```
$ docker-compose -f docker-compose-confluent-kafka.yml up -d
```

2. Start Control Center

<vm-hostname>:9021

- broker:29092
- <vm-hostname>:9092