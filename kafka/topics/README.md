# Creates kafka topics automatically.

## Parameters
`ZOOKEEPER_HOSTS` - zookeeper hosts,  I used value `"zookeeper:2181"` to run it locally.

`KAFKA_TOPICS` - space separated list of kafka topics. Example, `topic_1, topic_2, topic_3`.

Note, this container should run only **after** your original kafka broker and zookeeper are running.
After this container creates topics, it is not needed anymore.