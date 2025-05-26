FROM apache/spark-py:latest

WORKDIR /app

COPY main.py .

CMD ["/opt/spark/bin/spark-submit", "main.py"]