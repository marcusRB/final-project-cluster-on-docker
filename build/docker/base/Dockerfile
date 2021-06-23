ARG debian_buster_image_tag=8-jre-slim
FROM openjdk:${debian_buster_image_tag}
LABEL maintainer="MarcusRB <marcusrb@dataschool.tech>"

# -- Layer: Image Metadata

ARG build_date
ARG build_version

LABEL org.label-schema.build-date=${build_date} \
    org.label-schema.name="Final Project data architecture on Docker - Cluster base Image" \
    org.label-schema.description="Cluster base image" \
    org.label-schema.url="https://github.com/marcusRB/final-project-cluster-on-docker" \
    org.label-schema.schema-version=${build_version}


# -- Layer: OS + Python + Scala + r-base

ARG scala_version
ARG shared_workspace=/opt/workspace

RUN mkdir -p ${shared_workspace}/data && \
    mkdir -p /usr/share/man/man1 && \
    apt-get update -y && \
    apt-get install -y curl python3 r-base && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    curl https://downloads.lightbend.com/scala/${scala_version}/scala-${scala_version}.deb -k -o scala.deb && \
    apt install -y ./scala.deb && \
    rm -rf scala.deb /var/lib/apt/lists/*

ENV SCALA_HOME="/usr/bin/scala"
ENV PATH=${PATH}:${SCALA_HOME}/bin
ENV SHARED_WORKSPACE=${shared_workspace}

# -- Runtime

VOLUME ${shared_workspace}
CMD ["bash"]