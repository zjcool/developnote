1.查看kafka的消费情况
sh */bin/kafka-console-consumer.sh --topic <topticname> --zookeeper <zkip>

1.查看历史kafka的消费情况
sh */bin/kafka-console-consumer.sh --topic <topticname> --zookeeper <zkip> --from-beginning