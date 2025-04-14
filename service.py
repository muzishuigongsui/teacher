import pymysql
class PyMySQLUtils:
    def __init__(self):
        self.db=pymysql.connect(host='127.0.0.1',user='root',password='soul0816',database='school')
        # print(self.db)
        self.cursor=self.db.cursor()
    def fetchall(self,sql,*values):
        self.open()
        self.cursor.execute(sql,values)
        result=self.cursor.fetchall()
        self.close()
        return result

    def fetchone(self, sql, *values):
        self.open()
        self.cursor.execute(sql, values)
        result = self.cursor.fetchone()
        self.close()
        return result

    def execute(self,sql,values):
        try:
            self.open()
            self.cursor.execute(sql,values)
            self.db.commit()
            return 1
        except:
            self.db.rollback()
            return 0
        finally:
            self.close()

    def close(self):
        self.cursor.close()
        self.db.close()

    def open(self):
        self.db = pymysql.connect(host='127.0.0.1', user='root', password='soul0816', database='school')
        self.cursor = self.db.cursor()

if __name__=='__main__':
    datautil=PyMySQLUtils()
    # print(datautil.fetchone('SELECT COUNT(*) FROM teacher_login'))
    # print(datautil.fetchall('SELECT * FROM teacher_login'))
    sql='INSERT INTO teacher_login (loginname,loginpwd) VALUES (%s,%s);'
    values=('aaa','aaa')
    print(datautil.execute(sql, values))


















