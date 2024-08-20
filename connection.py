import pymysql
import pymysql.cursors
import json
import os
import traceback


class Connection:
    def __init__(self):
        self.config = self.read_config()
        self.conn = None
        self.cur = None
        self.connect()

    def read_config(self):
        with open(os.path.join(os.getcwd(), 'config.json'), 'r') as f:
            data = f.read()
            data = json.loads(data)
            f.close()
        return data

    def connect(self):
        self.conn = pymysql.connect(
            host=self.config['host'],
            user=self.config['user'],
            password=self.config['password'],
            db=self.config['db'],
            charset=self.config['charset'],
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=False
        )
        self.cur = self.conn.cursor()
        self.cur.execute(
            'set session autocommit=0;'
        )
        self.cur.execute(
            'set session transaction isolation level read committed;'
        )

    def execute(self, sql):
        try:
            self.cur.execute(sql)
            result = self.cur.fetchall()
            self.conn.commit()
            return result
        except Exception as e:
            self.conn.rollback()
            traceback.print_exc()
            print(f'==== execute error {e} ====')
        finally:
            self.disconnect()

    def disconnect(self):
        try:
            self.cur.close()
            self.conn.close()
        except Exception as e:
            traceback.print_exc()
            print(f'==== disconnect error {e} ====')
