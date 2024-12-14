# README

Little python script to convert the given tax at source from a txt file (inside of zip files) into a readable json file.

## How to use this tool

1. Go to [admin.ch](https://www.estv.admin.ch/estv/de/home/direkte-bundessteuer/dbst-quellensteuer/qst-tarife-loehne.html) website to download the "tax at source" datas to import into accounting systems
2. Download "Schweiz 20xx" as ZIP file (caution: this zip file contains a zip files for each canton with a `txt` file in it)
3. Extract the ZIP file and move the extracted ZIP files (the canton based zip files) from this ZIP file into the `source` folder
4. Execute this script (`python3 main.py` or via docker)
5. Check the output in the target folder - when script is finished, there should be only json files

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
