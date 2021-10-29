# Video Games List
![Capture d’écran du 2021-09-09 15-05-04](https://user-images.githubusercontent.com/33722914/132691149-7811732d-93af-4c87-8d4e-2577892497b6.png)

## Presentation:
Hello, this is a project named <b>video games list</b>, the goal of this project is to have a list of video games based on a <b>database</b> inside an application using <b>FastAPI</b>.
This project is split in three <b>docker container</b>: application, db and nginx, with a docker-compose.

![schema](https://user-images.githubusercontent.com/33722914/132901680-4455acb5-acd3-43be-9384-1a3da336b3f0.png)

### APP:
Web application FastAPI with:
* Route home on '/'
* Route video games list on '/games/all'
* Route video game detail '/games/1'
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

### NGINX
Proxy reverse with nginx run on port 80

## Architecture:
```
├── app
│   ├── api
│   │   ├── game.py
│   │   ├── home.py
│   │   ├── __init__.py
│   │   ├── ping.py
│   │   └── __pycache__
│   │       ├── game.cpython-37.pyc
│   │       ├── games.cpython-37.pyc
│   │       ├── home.cpython-37.pyc
│   │       ├── __init__.cpython-37.pyc
│   │       └── ping.cpython-37.pyc
│   ├── app.py
│   ├── config.py
│   ├── conn.py
│   ├── core
│   ├── Dockerfile
│   ├── Dockerfile.app
│   ├── entrypoint.sh
│   ├── htmlcov
│   │   ├── app_py.html
│   │   ├── config_py.html
│   │   ├── conn_py.html
│   │   ├── coverage_html.js
│   │   ├── d_10fae538ba4e8521_game_py.html
│   │   ├── d_10fae538ba4e8521_home_py.html
│   │   ├── d_10fae538ba4e8521___init___py.html
│   │   ├── d_10fae538ba4e8521_ping_py.html
│   │   ├── d_a44f0ac069e85531_conftest_py.html
│   │   ├── d_a44f0ac069e85531___init___py.html
│   │   ├── d_a44f0ac069e85531_test_games_py.html
│   │   ├── d_a44f0ac069e85531_test_home_py.html
│   │   ├── d_a44f0ac069e85531_test_ping_py.html
│   │   ├── d_e634d7a1dd90e049_game_py.html
│   │   ├── d_e634d7a1dd90e049_genre_py.html
│   │   ├── d_e634d7a1dd90e049___init___py.html
│   │   ├── favicon_32.png
│   │   ├── index.html
│   │   ├── __init___py.html
│   │   ├── jquery.ba-throttle-debounce.min.js
│   │   ├── jquery.hotkeys.js
│   │   ├── jquery.isonscreen.js
│   │   ├── jquery.min.js
│   │   ├── jquery.tablesorter.min.js
│   │   ├── keybd_closed.png
│   │   ├── keybd_open.png
│   │   ├── status.json
│   │   └── style.css
│   ├── __init__.py
│   ├── models
│   │   ├── game.py
│   │   ├── genre.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── game.cpython-37.pyc
│   │       ├── genre.cpython-37.pyc
│   │       └── __init__.cpython-37.pyc
│   ├── __pycache__
│   │   ├── app2.cpython-37.pyc
│   │   ├── app.cpython-37.pyc
│   │   ├── config.cpython-37.pyc
│   │   ├── conn.cpython-37.pyc
│   │   └── __init__.cpython-37.pyc
│   ├── requirements.txt
│   ├── static
│   │   └── styles.css
│   ├── templates
│   │   ├── games
│   │   │   ├── game.html
│   │   │   └── list.html
│   │   └── index.html
│   └── tests
│       ├── conftest.py
│       ├── __init__.py
│       ├── __pycache__
│       │   ├── conftest.cpython-37-pytest-6.2.4.pyc
│       │   ├── __init__.cpython-37.pyc
│       │   ├── test_games.cpython-37-pytest-6.2.4.pyc
│       │   ├── test_home.cpython-37-pytest-6.2.4.pyc
│       │   ├── test_ping.cpython-37-pytest-6.2.4.pyc
│       │   └── test_summaries.cpython-37-pytest-6.2.4.pyc
│       ├── test_games.py
│       ├── test_home.py
│       └── test_ping.py
├── db
│   ├── Dockerfile
│   ├── Dockerfile.db
│   └── sql
│       └── games.sql
├── docker-compose.yml
├── heroku.yml
├── letsencrypt
│   └── certs
├── nginx
│   └── Dockerfile.nginx
├── nginx.conf
├── Procfile
├── project
├── README.md
├── release.sh
├── setup.cfg
└── test
    └── test.sh
```
* App Folder
    * app.py with application
    * api folder with router
    * config.py with config for router
    * conn.py for sqlAlchemy connexion with db
    * Dockerfile build by docker-compose
    * Dockerfile.app dockerfile for heroku
    * requirements.txt to install modules needed
    * models folder with models for sqlalchemy
    * htmlcov with coverage report
    * tests folder for pytest
    * static with styles files
    * templates with html files
* DB folder
    * Dockerfile build by docker-compose
    * sql with our database
* docker-compose to run containers
* README.md it's me
* test folder for run tests
* nginx.conf with the configuration nginx
* .coveragerc for coverage config 
* heroku.yml for heroku config
* release.sh for deploy heroku


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
PORT=5000
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

## Heroku Deploiement
App and databases are on heroku. \
https://video-games-app1.herokuapp.com/

## Coverage/Quality
You can run come tests
### Pytest
```
docker-compose exec web python -m pytest --cov="."
```
### Flake
```
docker-compose exec web flake8 .
```
### Black
```
docker-compose exec web black .
```
### Isort
```
docker-compose exec web isort .
```
