from sqlalchemy import *
import pymysql

config = {
    'host': 'db',
    'port': 3306,
    'user': 'test',
    'password': 'test',
    'database': 'video_games'
}

db_user = config.get('user')
db_pwd = config.get('password')
db_host = config.get('host')
db_port = config.get('port')
db_name = config.get('database')

connection_str = "mysql+pymysql://{}:{}@{}:{}/{}".format(db_user, db_pwd, db_host, db_port, db_name)
engine = create_engine(connection_str)