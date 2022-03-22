## Start rabbitmq container (with management plugin):

$ docker run -d --network host --hostname my-rabbit --name some-rabbit rabbitmq:3-management


## Start mysql container:

$ docker run --network host --name some-mysql -e MYSQL_ROOT_PASSWORD=some-mysql -d mysql:latest


## Create a database and the required table

$ docker exec -it some-mysql mysql -uroot -p
Password: some-mysql

Use the commands from **create_db.sql** script to create the database and table.


## Build docker image and run container for the honeypot (server)

$ cd server/
$ docker build . -t honeypot/server
$ docker run -d --network host --name honeypot-server honeypot/server


## Build docker image and run container for consumer

$ cd consumer/
$ docker build . -t honeypot/consumer
$ docker run -d --network host --name honeypot-consumer honeypot/consumer


