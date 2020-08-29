import configparser
config = configparser.ConfigParser()
config['DEFAULT']={
'database': 'projectdb',
'host': 'localhost',
'user': 'root',
'password': ''
}
with open('config.ini', 'w') as configfile:
	config.write(configfile)