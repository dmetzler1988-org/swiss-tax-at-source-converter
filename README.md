# README

Little python script to convert the given tax at source from a txt file (inside of zip files) into a readable json file.

## Build and run for development

- Comment the PROD line in Dockerfile
- Uncomment the DEV lines in Dockerfile
- Execute `docker compose up --build -d --force-recreate`
- Switch into container `docker exec -it swiss-tax-at-source-converter-1 sh`
- Execute `python main.py`

## Without docker compose

```shell
# Build and start
docker build -q -t swiss-tax-at-source-converter:latest -f Dockerfile .
docker run -v `pwd`/target:/app/target --name swiss-tax-at-source-converter -d swiss-tax-at-source-converter:latest

# Remove
docker container rm -f swiss-tax-at-source-converter
```
