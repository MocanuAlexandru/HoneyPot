import pika
from flask import Flask, request, render_template

QUEUE_NAME = "server_requests"
channel = ""



# app = Flask('HoneyPot', root_path="/app/server")
app = Flask('HoneyPot')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def default_route(path):
    # # Get the parameters and build a path that contains them, too
    # params = request.args.to_dict()
    # requested_path = "/"
    # requested_path += path
    # str_params = '&'.join(map(lambda key: f"{key}={params[key]}", params))
    # if str_params != "": requested_path += "?"
    # requested_path += str_params

    # # Send the path to RabbitMQ
    # channel.basic_publish(
    #     exchange='',
    #     routing_key=QUEUE_NAME,
    #     body=requested_path,
    #     properties=pika.BasicProperties(
    #         delivery_mode = 2,
    #     )
    # )
    
    return render_template('HoneyPotPage.html')



def main():
    global channel

    # # Start the connection to RabbitMQ
    # with pika.BlockingConnection(pika.ConnectionParameters('localhost')) as connection:
    #     channel = connection.channel()

    #     # Declare the queue where the requests info will be send
    #     channel.queue_declare(QUEUE_NAME, durable=True)

    app.run(debug=True, port=5000, host='0.0.0.0')


if __name__ == '__main__':
    main()
