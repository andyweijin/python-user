__author__ = 'wei.jin'



import knowing.config.developconfig as config
import pypyodbc as sdb

class Connect():
    db_connect = None
    cursor  = None
    table = None
    where = None

    def  __init__(self):
        if not self.db_connect:

            self.db_connect=sdb.connect(config.SQL_CONNECT_STRING)

    def get_cursor(self):
        return self.db_connect.cursor()

    def get_execute(self,sql,**kwargs):
        cursor = self.get_cursor()
        return cursor.execute(sql,**kwargs)

    def get_rows(self,sql,**kwargs):
        if "limit" in kwargs:
            hang = kwargs.get('limit')
        else:
            hang = 1000
        return self.get_execute(sql).fetchmany(hang)

    def __del__(self):
        self.db_connect.close()
