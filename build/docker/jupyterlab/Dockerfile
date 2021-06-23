FROM mrussorb/cluster-base:debian_buster
LABEL maintainer="MarcusRB <marcusrb@dataschool.tech>"

# -- Layer: Image Metadata

ARG build_date
ARG build_version
ARG spark_version
ARG jupyterlab_version
ARG scala_kernel_version
ARG scala_version



LABEL org.label-schema.build-date=${build_date} \
    org.label-schema.name="Final Project data architecture on Docker - JupyterLab Image" \
    org.label-schema.description="JupyterLab image" \
    org.label-schema.url="https://github.com/marcusRB/final-project-cluster-on-docker" \
    org.label-schema.schema-version=${build_version}

# -- Layer: Notebooks and data

ADD workspace/ ${SHARED_WORKSPACE}/

# -- Layer: JupyterLab + Python kernel for PySpark


# -- New syntax python3 -m pip install <pkg>
RUN apt-get update -y && \
    apt-get install -y git-all python3-pip python3-dev && \
    pip3 install --upgrade pip && \
    pip3 install wget==3.2 pyspark==${spark_version} jupyterlab==${jupyterlab_version}

# -- Layer: Scala kernel for Spark

# ARG scala_version

RUN apt-get install -y ca-certificates-java --no-install-recommends && \
    curl -Lo coursier https://git.io/coursier-cli && \
    chmod +x coursier && \
    ./coursier launch --fork almond:${scala_kernel_version} --scala ${scala_version} -- --display-name "Scala ${scala_version}" --install && \
    rm -f coursier

# -- Layer: R kernel for SparkR

RUN apt-get install -y r-base-dev && \
    R -e "install.packages('IRkernel')" && \
    R -e "IRkernel::installspec(displayname = 'R 4.0.5', user = FALSE)" && \
    curl https://archive.apache.org/dist/spark/spark-${spark_version}/SparkR_${spark_version}.tar.gz -k -o sparkr.tar.gz && \
    R CMD INSTALL sparkr.tar.gz && \
    rm -f sparkr.tar.gz


# -- Additional Python packages

ADD requirements.txt .
RUN pip3 install -r requirements.txt --no-cache-dir -I --progress-bar emoji

# -- Runtime

EXPOSE 8888 5000

WORKDIR ${SHARED_WORKSPACE}
CMD jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token=
