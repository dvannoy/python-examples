# python-examples
Collection of basic examples using python
			
## s3_download.py
Sample of downloading a file from S3 using boto.				
## s3_upload.py
Sample of uploading a file to S3 using boto.
## sample_kafka_consumer.py
Simple kafka consumer that prints messages read from a topic.
## sample_kafka_producer.py
Simple kafka producer.
## sample_kafka_avro_consumer.py
Example that consumes avro formatted messages from Kafka.  Run by calling "python sample_kafka_avro_consumer.py topic_name schema_file_path" where the first argument is your kafka topic name and the second argument is a local path to an avro schema file.
## sample_kafka_confluent_avro_consumer.py
Example that consumes avro formatted messages from Kafka when confluent schema registry is used to store the avro schema info.  Run by calling "python sample_kafka_confluent_avro_consumer.py topic_name [reset]" where the first argument is your kafka topic name and the second argument is "reset" if you want to reprocess all available messages from the topic.
## sample_kafka_spark_streaming.py
Example using pyspark streaming that consumes avro formatted messages from Kafka when confluent schema registry is used to store the avro schema info.  This code prints to screen and writes the data to files.  Run by calling "spark-submit --master local [--jars spark-streaming-kafka-assembly_2.10-1.5.1.jar] sample_kafka_spark_streaming.py topic_name schema_registry_url" where the first argument is your kafka topic name and the second argument is the url for your schema registry (if local then you would enter http://localhost:8081)