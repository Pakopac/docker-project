# Video Games List

## Presentation:
Hello, this is a project named <b>video games list</b>, the goal of this project is to have a list of video games based on a <b>database</b> inside an application using <b>FastAPI</b>.
This project is split in two <b>docker container</b>: application and db, with a docker-compose.
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
...

