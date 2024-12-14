FROM python:alpine3.19

WORKDIR /app

COPY requirements.txt /app
RUN pip3 install -r requirements.txt

COPY .env.dist /app
COPY main.py /app

# FOR PROD
#CMD ["python3", "main.py"]

# FOR DEV
RUN pip3 install Flask==3.0.2
COPY server.py /app
EXPOSE 5000
CMD ["python3", "server.py"]
