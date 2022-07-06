# Replace <> fields in Kafka config
kafka_config = {
    "bootstrap.servers": "<host-name>.westus2.azure.confluent.cloud:9092",
    "security.protocol":"SASL_SSL",
    "sasl.mechanisms": "PLAIN",
    "sasl.username": "<confluent_api_username>",
    "sasl.password": "<confluent_api_password>"
}

# Replace <> fields in Twitter config
twitter_config = {
    "consumer_key": "<twitter_consumer_key>",
    "consumer_secret": "<twitter_consumer_secret>",
    "access_token": "<oauth_token>",
    "access_token_secret": "<oauth_secret>"
}