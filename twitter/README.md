
## Set environment variables
```
export COGNITIVE_SERVICE_KEY=<subscription_key>
export COGNITIVE_SERVICE_ENDPOINT=https://<service-name>.cognitiveservices.azure.com/
```

## Build Docker container
`docker build -t tech-twitter-producer .`

## Run local
`docker run --rm -it tech-twitter-producer`

## Azure setup (one-time)
Create resource group
`az group create --name data-streaming-rg --location westus2`

Create Azure Container registry
`az acr create --resource-group data-streaming-rg --name datastreamcr --sku Basic --admin-enabled`

Login to Azure Container registry and get login server name
```
az acr login --name datastreamcr --expose-token
az acr list --resource-group data-streaming-rg --output table
```

Find the image id
`docker images`

Tag docker image by adding login server and push
```
docker tag tech-twitter-producer datastreamcr.azurecr.io/tech-twitter-producer:v1
# docker login datastreamcr.azurecr.io -u 00000000-0000-0000-0000-000000000000 -p <access-token>
docker push datastreamcr.azurecr.io/tech-twitter-producer:v1
```

Create and start container instance
```
az acr credential show --name datastreamcr
az container create --resource-group data-streaming-rg --name techtwitterdemo --image datastreamcr.azurecr.io/tech-twitter-producer:v1 --cpu 1 --memory 1 --ip-address Private --vnet data-streaming-vnet --subnet data-streaming-subnet
```