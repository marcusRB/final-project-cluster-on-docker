# Final Project - Cluster on Docker 
```
PRO env. [Version 1.1.0](/#Control Versioning)

```

## Abstract

This final work shows a viable data architecture solution to address the fraud detection use case of the insurance sector, in the same way to see how to analyse the features for the creation of a fraud prediction model. We will proceed with the design of the architecture, analyse the data pipeline in two temporal moments, batch mode and streaming mode, and finally, shows the results. As complement of that, it will be the comparison between different data treatment processes, study the different ways to consider the start-up phase and to detect possible risks. The aim of the work is to be able to combine data architecture, opting for a hybrid method between Lambda and Kappa architecture, in addition using microservices technology based on Docker and machine learning monitoring by MLOps methods and GitHub workflow.

***

### Architecture Design

- [X] Lambda Architecture
- [X] Kappa Architecture

### Implementation and configuration

- [X] Dockerfile // Docker build

### Microservices and ports

- [X] Spark -> master 7077, 4044 - workers 8081, 8082, 8083
- [X] Kafka standalone -> 9091
- [X] Kafka by Confluent stack -> 19092 / 29092 / 9092
- [X] MongoDB -> 27017, 27018, 27019
- [X] PostgreSQL -> 5432, 15432, 25432
- [X] NodeJS
- [X] Grafana -> 3000
- [X] Prometheus -> 9090
- [ ] R Studio (pending due version conflict server/livy on Spark 3.1.1)
- [X] JupyterLab Notebook -> 8888
- [X] Zeppelin Notebook -> 7081
- [X] MLflow -> 5000
- [ ] Superset (pending due port conflict) -> 8088

## Other databases next release

- [ ] HBase (next release)
- [ ] Hive (next release)
- [ ] Cassandra (next release)
- [ ] Druid (next release)

***

## Jupyter notebooks, code, Proof of Concept

- [X] Examples on Spark
- [X] Examples Kafka to Spark
- [X] Kafka consumer and producer on PySpark
- [X] Porto Seguro's prediction claim on Python
- [X] Porto Seguro's prediction claim on PySpark
- [X] Porto Seguro's prediction claim on Databricks
- [X] Machine Learning MLflow
- [ ] Streaming processing (pending)
- [X] ML codes on Python

***

## Guide available here

### SETUP Git & Docker Compose last version on 
> test made on VM Linux

1. Clone master repository

```{bash}
$ git clone https://<repository-url>
```

2. Check Docker-Compose or install

```{bash}
$ apt install docker-compose
```

3. Start **main cluster** Kafka and Spark (Simulation)

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

***

## Start Kafka by Confluent & Spark - MongoDB & other databases

1. Start Docker-Compose

```
# Start Confluent services
$ docker-compose -f docker-compose-confluent-kafka.yml up -d
```

```
# Start Spark services
$ docker-compose -f docker-compose-cluster-spark.yml up -d
```

```
# Start MongoDB replicas
$ docker-compose -f docker-compose-mongodb.yml up -d
```

2. Start Control Center

<vm-hostname>:9021

- broker:29092
- <vm-hostname>:9092

3. Start Jupyter Notebook

<vm-hostname>:8888

***

## Start Notebooks containers - Jupyter & Zeppelin


1. Launch docker-compose command

```{sh}
$ docker-compose -f docker-compose-notebooks.yml up -d
```

***

## Kafka simulation part I

Inside Jupyter environment execute:


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



***
[## Control Versioning]
```
# - 1.1.0 > 01.07.2021 (add Zeppelin notebook, change Superset port)
#
#
#