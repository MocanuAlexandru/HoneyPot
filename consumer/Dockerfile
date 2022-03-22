FROM python:latest
COPY . /app/consumer
RUN pip install -r /app/consumer/requirements.txt
CMD python /app/consumer/worker.py
