from mysql.connector.errors import Error
import os ,time,configparser,mysql.connector
from multipledispatch import dispatch 
class Db_Class(object):
	def __init__(self):
		self.Db_name=""
		self.Host=""
		self.User=""
		self.Pw=""
		self.Db_Status=0
		self.Get_Config()
	
	def Get_Config(self):
		config = configparser.ConfigParser()
		if not os.path.isfile("config.ini"):
			self.Create_Default_Config()
		config.read('config.ini')
		self.Db_name=config['DEFAULT']['database']
		self.Host=config['DEFAULT']['host']
		self.User=config['DEFAULT']['user']
		self.Pw=config['DEFAULT']['password']
		del config

	def Create_Default_Config(self):
		self.Db_name="projectdb"
		self.Host="localhost"
		self.User="root"
		self.Pw=""
		self.Create_Config()

	def Create_Config(self):
		config = configparser.ConfigParser()
		config['DEFAULT']={
		'database': self.Db_name,
		'host': self.Host,
		'user': self.User,
		'password': self.Pw
		}
		with open('config.ini', 'w') as configfile:
			config.write(configfile)
		del config

	def Check_Db_Status(self):
		self.Db_Status=self.Db_Check()

	def Db_Check(self):
		try:
			self.mydb = mysql.connector.connect(
			host=self.Host,
			user=self.User,
			passwd=self.Pw,
			database=self.Db_name
			)
			self.mycursor=self.mydb.cursor()
			return 1
		except mysql.connector.Error as e:
			if e.errno==1049:
				return 0
			elif e.errno==2003:
				return -1
			else:
				return e
	def Db_Create(self):
		try:
			mydb=mysql.connector.connect(
			host=self.Host,
			user=self.User,
			passwd=self.Pw,
			)
			mycursor = mydb.cursor()
			mycursor.execute("CREATE DATABASE {}".format(self.Db_name))
			del mycursor
			del mydb
			return 1
		except mysql.connector.Error as e:
			return e

	def Import_Db(self):
		try:
			f=open("projectdb.sql","r")
			for line in f:
				self.mycursor.execute(line)
			f.close()
			del f
			return 1
		except mysql.connector.Error as e:
			return e

	def Ders_insert(self,txt):
		try:
			sql="INSERT INTO `ders` (`Ders_id`, `Ders_adi`) VALUES (%s, %s);"
			val=("NULL",txt)
			self.mycursor.execute(sql,val)
			self.mydb.commit()
		except Exception as e:
			raise e

	def Ders_get_all(self):
		try:
			sql="SELECT * FROM ders"
			self.mycursor.execute(sql)
			x=self.mycursor.fetchall()			
			return x
		except Exception as e:
			raise e
	def Konu_get(self,index):
		try:
			sql="SELECT * FROM konu WHERE Ders_Konu_id="+str(index)
			self.mycursor.execute(sql)
			x=self.mycursor.fetchall()			
			return x
		except Exception as e:
			raise e		
	def Ders_search(self,txt):
		try:
			sql="SELECT * FROM ders WHERE  Ders_adi like '%"+txt+"%'"
			self.mycursor.execute(sql)
			x=self.mycursor.fetchall()			
			return x
		except Exception as e:
			raise e		
	def Konu_get_all(self):
		try:
			sql="SELECT  konu.Konu_id,ders.Ders_adi,konu.Donem,konu.Konu_adi FROM ders INNER JOIN konu ON ders.Ders_id = konu.Ders_Konu_id"
			self.mycursor.execute(sql)
			x=self.mycursor.fetchall()			
			return x
		except Exception as e:
			raise e		
	def Ders_update(self,did,txt):
		try:
			sql="UPDATE ders SET Ders_adi=%s WHERE Ders_id=%s;"
			val=(txt,did)
			self.mycursor.execute(sql,val)
			self.mydb.commit()
		except Exception as e:
			raise e
	def Konu_insert(self,did,donem,ad):
		try:
			sql="INSERT INTO `konu` (`Konu_id`, `Konu_adi` , `Donem` , `Ders_Konu_id` ) VALUES (%s, %s , %s , %s);"
			val=("NULL",ad,donem,did)
			self.mycursor.execute(sql,val)
			self.mydb.commit()
		except Exception as e:
			raise e
	def Konu_search(self,txt):
		try:
			txt="%"+txt+"%"
			sql="SELECT  konu.Konu_id,ders.Ders_adi,konu.Donem,konu.Konu_adi FROM ders INNER JOIN konu ON ders.Ders_id = konu.Ders_Konu_id WHERE  Konu_adi like %s OR ders.Ders_adi like %s"
			val=(txt,txt)
			self.mycursor.execute(sql,val)
			x=self.mycursor.fetchall()	
			return x
		except Exception as e:
			raise e
	def Konu_update(self,kid,did,donem,txt):
		try:
			sql="UPDATE konu SET Konu_adi=%s , Donem=%s , Ders_Konu_id=%s WHERE Konu_id=%s;"
			val=(txt,donem,did,kid)
			self.mycursor.execute(sql,val)
			self.mydb.commit()
		except Exception as e:
			raise e
	def Soru_insert(self,kid,txt):
		try:
			sql="INSERT INTO `soru` (`Soru_Konu_id`, `Soru_icerik`) VALUES (%s, %s);"
			val=(kid,txt)
			self.mycursor.execute(sql,val)
			self.mydb.commit()
		except Exception as e:
			raise e
	def Soru_get_all(self):
		try:
			sql="SELECT soru.Soru_id,ders.Ders_adi,konu.Konu_adi,soru.Soru_icerik FROM `soru` INNER JOIN konu ON soru.Soru_Konu_id=konu.Konu_id INNER JOIN ders ON konu.Ders_Konu_id=ders.Ders_id"
			self.mycursor.execute(sql)
			x=self.mycursor.fetchall()			
			return x
		except Exception as e:
			raise e
	def Soru_update(self,sid,kid,stext):
		try:
			sql="UPDATE soru SET Soru_Konu_id=%s , Soru_icerik=%s WHERE Soru_id=%s;"
			val=(kid,stext,sid)
			self.mycursor.execute(sql,val)
			self.mydb.commit()
		except Exception as e:
			raise e
	def Soru_search(self,stext,konutext):
		try:
			sql="SELECT soru.Soru_id,ders.Ders_adi,konu.Konu_adi,soru.Soru_icerik FROM `soru` INNER JOIN konu ON soru.Soru_Konu_id=konu.Konu_id INNER JOIN ders ON konu.Ders_Konu_id=ders.Ders_id WHERE soru.Soru_icerik LIKE %s AND konu.Konu_adi LIKE %s;"
			val=(stext,konutext)
			self.mycursor.execute(sql,val)
			x=self.mycursor.fetchall()	
			return x
		except Exception as e:
			print(str(e))
			raise e
	@dispatch()
	def Soru_count(self):
		try:
			sql="SELECT COUNT(soru.Soru_id),ders.Ders_adi FROM `soru` INNER JOIN konu ON soru.Soru_Konu_id=konu.Konu_id INNER JOIN ders ON konu.Ders_Konu_id=ders.Ders_id GROUP BY Ders_adi"
			self.mycursor.execute(sql)
			x=self.mycursor.fetchall()	
			return x
		except Exception as e:
			print(str(e))
			raise e
	@dispatch(int)
	def Soru_count(self,kid):
		try:
			sql="SELECT COUNT(soru_id) FROM soru WHERE Soru_Konu_id=%s"
			val=(kid,)
			self.mycursor.execute(sql,val)
			x=self.mycursor.fetchall()	
			return x[0][0]
		except Exception as e:
			print(str(e))
			raise e
	@dispatch(str)
	def Konu_count(self,kad):
		try:
			sql="SELECT COUNT(konu.Konu_id),konu.Konu_adi FROM `soru` INNER JOIN konu ON soru.Soru_Konu_id=konu.Konu_id INNER JOIN ders ON konu.Ders_Konu_id=ders.Ders_id WHERE Ders_adi='"+kad+"' GROUP BY konu_adi"
			self.mycursor.execute(sql)
			x=self.mycursor.fetchall()	
			return x
		except Exception as e:
			print(str(e))
			raise e
	@dispatch(int,int)
	def Konu_count(self,did,donem):
		try:
			if donem==2:
				sql="SELECT COUNT(konu.Konu_id) FROM `konu` WHERE Ders_Konu_id=%s"
				val=(did,)
			else:
				sql="SELECT COUNT(konu.Konu_id) FROM `konu` INNER JOIN ders ON konu.Ders_Konu_id=ders.Ders_id WHERE Ders_id=%s AND Donem=%s"
				val=(did,donem)
			self.mycursor.execute(sql,val)
			x=self.mycursor.fetchall()	
			return x[0][0]
		except Exception as e:
			print(str(e))
			raise e
	def get_exams_subjects(self,did,donem):
		try:
			if int(donem)==2:
				sql="SELECT Konu_id,Konu_adi FROM konu WHERE Ders_Konu_id=%s"
				val=(did,)
			else:
				sql="SELECT Konu_id,Konu_adi FROM konu WHERE Ders_Konu_id=%s AND Donem=%s"
				val=(did,donem)
			self.mycursor.execute(sql,val)
			x=self.mycursor.fetchall()
			return x
		except Exception as e:
			print(str(e))
			raise e
		
	def check_exam_is_suitable(self,did,donem):
		try:
			if int(donem)==2:
				sql="SELECT COUNT(soru.Soru_id) FROM `soru` INNER JOIN konu ON soru.Soru_Konu_id=konu.Konu_id INNER JOIN ders ON konu.Ders_Konu_id=ders.Ders_id WHERE Ders_id=%s"
				val=(did,)
			else:
				sql="SELECT COUNT(soru.Soru_id) FROM `soru` INNER JOIN konu ON soru.Soru_Konu_id=konu.Konu_id INNER JOIN ders ON konu.Ders_Konu_id=ders.Ders_id WHERE Ders_id=%s AND Donem=%s"
				val=(did,donem)
			self.mycursor.execute(sql,val)
			x=self.mycursor.fetchall()
			return int(x[0][0])
		except Exception as e:
			print(str(e))
			raise e
	@dispatch(int,int,int)
	def get_random_exam(self,did,donem,sayi):
		try:
			if int(donem)==2:
				sql="SELECT soru.Soru_icerik FROM `soru` INNER JOIN konu ON soru.Soru_Konu_id=konu.Konu_id INNER JOIN ders ON konu.Ders_Konu_id=ders.Ders_id WHERE Ders_id=%s ORDER BY RAND() LIMIT %s"
				val=(did,sayi)
			else:
				sql="SELECT soru.Soru_icerik FROM `soru` INNER JOIN konu ON soru.Soru_Konu_id=konu.Konu_id INNER JOIN ders ON konu.Ders_Konu_id=ders.Ders_id WHERE Ders_id=%s AND Donem=%s ORDER BY RAND() LIMIT %s"
				val=(did,donem,sayi)
			self.mycursor.execute(sql,val)
			x=self.mycursor.fetchall()	
			return x
		except Exception as e:
			print(str(e))
			raise e	
	@dispatch(int,int)
	def get_random_exam(self,kid,sayi):
		try:
			sql="SELECT Soru_icerik,Soru_id FROM `soru` WHERE Soru_Konu_id=%s ORDER BY RAND() LIMIT %s"
			val=(kid,sayi)
			self.mycursor.execute(sql,val)
			x=self.mycursor.fetchall()	
			return x
		except Exception as e:
			print(str(e))
			raise e
	@dispatch(int,int,list)
	def get_random_exam(self,did,sayi,selectedquestions):
		try:
			print(sayi)
			print(selectedquestions)
			sql="SELECT soru.Soru_icerik,soru.Soru_id FROM `soru` INNER JOIN konu ON soru.Soru_Konu_id=konu.Konu_id INNER JOIN ders ON konu.Ders_Konu_id=ders.Ders_id WHERE Ders_id=%s AND soru.Soru_id NOT IN {} ORDER BY RAND() LIMIT %s".format(tuple(selectedquestions))
			val=(did,sayi)
			self.mycursor.execute(sql,val)
			x=self.mycursor.fetchall()	
			return x
		except Exception as e:
			print(str(e))
			raise e		
	def delete_soru(self,sid):
		try:
			sql="DELETE FROM `soru` WHERE `soru`.`Soru_id` = %s"
			val=(sid,)
			self.mycursor.execute(sql,val)
			self.mydb.commit()
			return 1
		except Exception as e:
			return e
	def delete_konu(self,kid):
		try:
			sql="DELETE FROM soru WHERE Soru_Konu_id=%s"
			val=(kid,)
			self.mycursor.execute(sql,val)
			self.mydb.commit()
			sql="DELETE FROM konu WHERE Konu_id=%s"
			val=(kid,)
			self.mycursor.execute(sql,val)
			self.mydb.commit()
			return 1
		except Exception as e:
			return e
	def delete_ders(self,did):
		try:
			sql="DELETE FROM ders WHERE ders.Ders_id=%s;"
			val=(did,)
			self.mycursor.execute(sql,val)
			self.mydb.commit()
			return 1
		except Exception as e:
			return e