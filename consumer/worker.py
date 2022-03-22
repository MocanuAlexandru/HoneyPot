#!/usr/bin/env python
import pika
import time
import mysql.connector

DATABASE = 'HoneyPotDB'
QUEUE_NAME = 'server_requests'


with pika.BlockingConnection(pika.ConnectionParameters('localhost')) as rabbitmq_connection, \
     mysql.connector.connect(user='root', password='some-mysql', host='localhost', database=DATABASE) as mysql_connection, \
     mysql_connection.cursor() as cursor:
    channel = rabbitmq_connection.channel()

    channel.queue_declare(queue=QUEUE_NAME, durable=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body.decode())
        str_path = body.decode()
        cursor.execute("INSERT INTO requests(path) VALUES (%s)", (str_path,))
        mysql_connection.commit()
        id_no = cursor.lastrowid
        print(id_no)
        print(" [x] Done")
        ch.basic_ack(delivery_tag = method.delivery_tag)



    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback)

    channel.start_consuming()
