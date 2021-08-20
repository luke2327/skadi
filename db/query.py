import pymysql.cursors
import json


def connect_db():
    with open('lib/db_config.json', 'r', encoding='utf-8') as db_config:
        db_config = json.load(db_config)

        conn = pymysql.connect(
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password'],
            db=db_config['db'],
            charset='utf8'
        )

    curs = conn.cursor()

    return {'curs': curs, 'conn': conn}


def execute(query):
    connect_info = connect_db()
    conn = connect_info['conn']
    curs = connect_info['curs']

    try:
        curs.execute(query)

        conn.commit()

    finally:
        conn.close()
