import pymysql 

def mysqlconnect(): 
	# To connect MySQL database 
	conn = pymysql.connect( 
			host='localhost', 
			user='root', 
			password = "root", 
			db='mqtt_db',
			)
	cur=conn.cursor()
	sql="INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
	cur.execute(sql, ('Barun@gmail.com', 'secret'))
	conn.commit()
	cur.execute("select * from `users`")
	output = cur.fetchall()
	print(output) 
	# To close the connection
	conn.close()

def mysqlInsert():
	# To connect MySQL database 
	conn = pymysql.connect( 
			host='localhost', 
			user='root', 
			password = "root", 
			db='mqtt_db',
			)
	cur=conn.cursor()
	sql="INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
	cur.execute(sql, ('Arun@gmail.com', 'secret'))
	conn.commit()
	# To close the connection
	conn.close()

def mysqlQuery():
	# To connect MySQL database 
	conn = pymysql.connect( 
			host='localhost', 
			user='root', 
			password = "root", 
			db='mqtt_db',
			)
	cur=conn.cursor()
	cur.execute("select * from `users`")
	output = cur.fetchall()
	print(output) 
	# To close the connection
	conn.close() 

# Driver Code 
if __name__ == "__main__" :
	mysqlconnect()
	#mysqlInsert()
	#mysqlQuery()