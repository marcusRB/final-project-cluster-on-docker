# It is recommened to use same version as kafka broker is used.
# So no additional images are pulled.
FROM confluentinc/cp-kafka:${KAFKA_VERSION}

WORKDIR usr/bin

# Once it is executed, this container is not needed.
COPY kafka-topics.sh kafka-topics.sh
ENTRYPOINT ["./kafka-topics.sh"]
