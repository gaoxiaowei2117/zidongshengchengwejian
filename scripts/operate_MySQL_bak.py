import pymysql

#指定数据库地址、用户、密码、端口，使用connect()方法声明一个Mysql连接对象db
db = pymysql.connect(host='localhost',user='root', password='Nc480s><ltyyz', port=3306, db="91Creater")

#调用cursor()方法获得Mysql的操作游标，利用游标来执行SQL语句。
cursor = db.cursor()

#直接用execute()方法执行，第一句用于获得Mysql版本，然后调用fetchone()方法获得第一条数据。
#cursor.execute('SELECT VERSION()')
#data = cursor.fetchone()
#print('Database version:', data)

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


db.close()

if __name__ == "__main__":
    
