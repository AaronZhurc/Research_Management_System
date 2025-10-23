import pymysql
class Userbean:
    def __init__(self,uname):
        db = pymysql.connect("localhost", "root", "db120325", "test")
        sql = "select * from secuser where uname=\'" + uname + "\'"
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchone()
        self.uname=data[1]
        self.password=data[2]
        self.authority=data[3]
        self.school=data[4]
        self.position=data[5]
        self.name=data[6]
