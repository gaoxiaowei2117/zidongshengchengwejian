import os
import re
import sys
import pymysql

class MyMysql(object):
    def __init__(self, myHost, myUser, myPasswd, myPort, myDB):
        #指定数据库地址、用户、密码、端口，使用connect()方法声明一个Mysql连接对象db
        #self.__db = pymysql.connect(host='localhost',user='root', password='Nc480s><ltyyz', port=3306, db="91Creater")
        self.__db = pymysql.connect(host=myHost,user=myUser, password=myPasswd, port=myPort, db=myDB)
        #调用cursor()方法获得Mysql的操作游标，利用游标来执行SQL语句。
        self.cursor = self.__db.cursor()

    def __del__(self):
        self.__db.close()
    
    def CreatePassage(self, userID):
        sql = 'select count(*) from passages_'+userID
        try:
            self.cursor.execute(sql)
        except:
            try:
                sql = 'CREATE TABLE IF NOT EXISTS passages_' + userID + '(passagesID INT NOT NULL auto_increment, userID INT NOT NULL, productID INT NOT NULL, passages TEXT NOT NULL, PRIMARY KEY (passagesID))'
                self.cursor.execute(sql)
            except:
                print("Error: unable to create table")

    def InsertPassages(self, userID, productID, contentList):
        for content in contentList:
            sql = 'insert into passages_' + userID + ' (userID, productID, passages) value(' + userID +', ' + productID + ', "' + content + '")'
            try:
                self.cursor.execute(sql)
                self.__db.commit()
            except:
                self.__db.rollback()

    def SelectPassages(self, userID, productID):
        sql = 'select passages from passages_' + userID + ' where productID = ' + productID
        #print(sql)
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            #print([str(i[0]) for i in results])
            return ([str(i[0]) for i in results])
            #return results
        except:
            print("Error: unable to select data from passages_%s"%userID)

    def InsertPicture(self, userID, productID, pictureList):
        for url in pictureList:
            sql = 'insert into pictures (userID, productID, pictureUrl) value(' + userID +', ' + productID + ', "' + url + '")'
            try:
                self.cursor.execute(sql)
                self.__db.commit()
            except:
                self.__db.rollback()
            
    def SelectPicture(self, userID, productID):
        sql = 'select pictureUrl from pictures where userID = ' + userID + ' and productID = ' + productID
        #print(sql)
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            #print([str(i[0]) for i in results])
            return ([str(i[0]) for i in results])
            #return results
        except:
            print("Error: unable to select data from passages_%s"%userID)

    def SelectProduct(self, userID, productID):
        sql = 'select productName from products where userID = ' + userID + ' and productID = ' + productID
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            print([str(i[0]) for i in results])
            return ([str(i[0]) for i in results])
            #return results
        except:
            print("Error: run (%s)"%sql)

    def SelectTasks(self):
        #sql = 'select taskID, userID, productID, times, first_keywords, second_keywords, third_keywords from tasks where status = 1'
        sql = 'select t.taskID, t.userID, t.productID, t.times, t.first_keywords, t.second_keywords, t.third_keywords, u.userAuth, u.userCookie, u.userUA from tasks t inner join users u where t.status = 1 and t.userID = u.userID'
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            #print(results)
            return results
        except:
            print("Error: unable to select data from tasks")
        

    def ShowVersion(self):
        #直接用execute()方法执行，第一句用于获得Mysql版本，然后调用fetchone()方法获得第一条数据。
        self.cursor.execute('SELECT VERSION()')
        data = self.cursor.fetchone()
        print('Database version:', data)
'''
sql = 'select count(*) from passages_1'
#sql = 'select * from customize_passages'
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   #results = cursor.fetchall()
   #for row in results:
   #     print(row)
     
except:
   print("Error: unable to fecth data")
sql = 'CREATE TABLE IF NOT EXISTS passages_1 (passagesID INT NOT NULL auto_increment, userID INT NOT NULL, productID INT NOT NULL, passages TEXT NOT NULL, PRIMARY KEY (passagesID))'
try:
    cursor.execute(sql)
except:
    print("Error: unable to create table")
'''


if __name__ == "__main__":
    userID = sys.argv[1]
    productID = sys.argv[2]
    fileName = sys.argv[3]
    db = MyMysql(myHost='localhost',myUser='root', myPasswd='Nc480s><ltyyz', myPort=3306, myDB="91Creater")
    db.CreatePassage(userID)

    p=re.compile('\n',re.S);
    f= open(fileName,'r',encoding='utf8')
    fileContent = f.read()
    phasesList=p.split(fileContent)
    #print(phasesList)
    f.close()
    
    if 'pictures' == os.path.basename(fileName):
        db.InsertPicture(userID, productID, phasesList[0:-1])
    elif 'phases' == os.path.basename(fileName):
        db.InsertPassages(userID, productID, phasesList[0:-1])
    #db.SelectPassages(userID, '1')
    #db.SelectPicture(userID, '1')
    #db.SelectProduct(userID, '1')

     
