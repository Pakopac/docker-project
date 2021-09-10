# Video Games List
![Capture d’écran du 2021-09-09 15-05-04](https://user-images.githubusercontent.com/33722914/132691149-7811732d-93af-4c87-8d4e-2577892497b6.png)

## Presentation:
Hello, this is a project named <b>video games list</b>, the goal of this project is to have a list of video games based on a <b>database</b> inside an application using <b>FastAPI</b>.
This project is split in two <b>docker container</b>: application and db, with a docker-compose.

![schema](https://user-images.githubusercontent.com/33722914/132901680-4455acb5-acd3-43be-9384-1a3da336b3f0.png)

### APP:
Web application FastAPI with:
* Route home on '/'
* Route video games list on '/list'
* Get from db with sqlAlchemy
* Templates with Jinja
* Run on port 5000

### DATABASE:
MySQL Database

```
+-----------------------+
| Tables_in_video_games |
+-----------------------+
| game                  |
| game_platform         |
| game_publisher        |
| genre                 |
| platform              |
| publisher             |
| region                |
| region_sales          |
+-----------------------+
```
Run on port 3306

## Architecture:
```
├── app
│   ├── app.py
│   ├── conn.py
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── static
│   │   └── styles.css
│   └── templates
│       └── index.html
├── db
│   ├── Dockerfile
│   └── sql
│       └── games.sql
├── docker-compose.yml
└── README.md
```

* App Folder
    * app.py with application
    * conn.py for sqlAlchemy connextion with db
    * Dockerfile build by docker-compose
    * requirements.txt to install modules needed
    * static with styles files
    * templates with html files
* DB folder
    * Dockerfile build by docker-compose
    * sql with our database
* docker-compose to run containers
* README.md it's me


## Install
First you need to clone the repository:
```
git clone git@github.com:Pakopac/docker-project.git
```
then:
```
cd project-docker
```
Make sure you have docker install with the corrects rights: https://docs.docker.com/get-docker/

Make sure mysql is not running on port 3306, to shut down it:
```
sudo service mysql stop
```
Create .env file with username and password for the database:
```
touch .env
```
```
.env

SQL_USER=your_username
SQL_PASSWORD=your_password
```

You can build containers:
```
docker-compose build
```
The result:
```
Building db
Step 1/1 : FROM mysql:5.7
 ---> d54bd1054823

Successfully built d54bd1054823
Successfully tagged project-docker_db:latest
Building web
Step 1/6 : FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
 ---> 86ade7dea2c7
Step 2/6 : COPY requirements.txt .
 ---> Using cache
 ---> 0aea53f45231
Step 3/6 : RUN pip install -r requirements.txt
 ---> Using cache
 ---> c604be5c44b0
Step 4/6 : EXPOSE 5000
 ---> Using cache
 ---> 923d508fc995
Step 5/6 : COPY . .
 ---> 0905ac01d9ac
Step 6/6 : CMD ["gunicorn", "app:app", "-w", "3", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:5000"]
 ---> Running in d7937e0e1c2f
Removing intermediate container d7937e0e1c2f
 ---> 94af7a05a92b

Successfully built 94af7a05a92b
Successfully tagged project-docker_web:latest
```
And run:
```
docker-compose up -d
```
Check if your containers are running
```
docker ps
```
If you have something like this it's ok !
```
CONTAINER ID   IMAGE                COMMAND                  CREATED         STATUS          PORTS                               NAMES
629a053ec5d4   project-docker_web   "gunicorn app:app -w…"   4 minutes ago   Up 22 seconds   80/tcp, 0.0.0.0:5000->5000/tcp      project-docker_web_1
186ecaee81ed   project-docker_db    "docker-entrypoint.s…"   4 minutes ago   Up 4 minutes    0.0.0.0:3306->3306/tcp, 33060/tcp   project-docker_db_1
48024c68420c   redis                "docker-entrypoint.s…"   4 minutes ago   Up 4 minutes    6379/tcp                            project-docker_redis-container_1
```

Check on your browser: http://localhost:5000/

## Test
Run tests to check if yours containers are ok
```
sh test/test.sh
```
You need to have something like that
```
--- Docker Container ---
CONTAINER ID   IMAGE                     COMMAND                  CREATED         STATUS                            PORTS                               NAMES
39cffdde787e   pakopac/video_games_db    "docker-entrypoint.s…"   2 minutes ago   Up 2 minutes (health: starting)   0.0.0.0:3306->3306/tcp, 33060/tcp   video_games_db_1
c186840aafc4   pakopac/video_games_app   "./entrypoint.sh gun…"   2 minutes ago   Up 2 minutes (health: starting)   80/tcp, 0.0.0.0:5000->5000/tcp      video_games_app_1
9f96d4b65729   redis                     "docker-entrypoint.s…"   3 minutes ago   Up 2 minutes                      6379/tcp                            video_games_redis-container_1
--- DB ---
[2021-09-10 12:14:56 +0000] [77] [INFO] Booting worker with pid: 77
[2021-09-10 12:15:05 +0000] [75] [INFO] Started server process [75]
[2021-09-10 12:15:05 +0000] [75] [INFO] Waiting for application startup.
[2021-09-10 12:15:05 +0000] [75] [INFO] Application startup complete.
[2021-09-10 12:15:05 +0000] [77] [INFO] Started server process [77]
[2021-09-10 12:15:05 +0000] [77] [INFO] Waiting for application startup.
[2021-09-10 12:15:05 +0000] [77] [INFO] Application startup complete.
[2021-09-10 12:15:05 +0000] [76] [INFO] Started server process [76]
[2021-09-10 12:15:05 +0000] [76] [INFO] Waiting for application startup.
[2021-09-10 12:15:05 +0000] [76] [INFO] Application startup complete.
--- APP ---
2021-09-10T12:14:53.240940Z 0 [Note]   - '::' resolves to '::';
2021-09-10T12:14:53.241114Z 0 [Note] Server socket created on IP: '::'.
2021-09-10T12:14:53.242438Z 0 [Note] InnoDB: Buffer pool(s) load completed at 210910 12:14:53
2021-09-10T12:14:53.299882Z 0 [Warning] Insecure configuration for --pid-file: Location '/var/run/mysqld' in the path is accessible to all OS users. Consider choosing a different directory.
2021-09-10T12:14:53.308168Z 0 [Note] Event Scheduler: Loaded 0 events
2021-09-10T12:14:53.308272Z 0 [Note] Execution of init_file '/docker-entrypoint-initdb.d/games.sql' started.
2021-09-10T12:15:05.150042Z 0 [Note] Execution of init_file '/docker-entrypoint-initdb.d/games.sql' ended.
2021-09-10T12:15:05.150459Z 0 [Note] mysqld: ready for connections.
Version: '5.7.33'  socket: '/var/run/mysqld/mysqld.sock'  port: 3306  MySQL Community Server (GPL)
```

## Docker-hub

Get images from docker-hub\
https://hub.docker.com/repository/docker/pakopac/video_games_app
https://hub.docker.com/repository/docker/pakopac/video_games_db
