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