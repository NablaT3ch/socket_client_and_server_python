from socket import *
import os
import sys

host='0.0.0.0'
port=1112

def connect():
	server=socket(AF_INET,SOCK_STREAM)
	server.bind((host,port))
	server.listen(2)
	print("[*] listening on %s:%d" %(host,port))

	conn,addr=server.accept()
	print("accepted connection from %s:%d" %(addr[0],addr[1]))
	
	while True:

		data=conn.recv(1024)
		data=data.decode()
		print("client Run %s" %data)
		if 'show_files' in data:
			req=fileList()
			conn.send(req.encode())
		elif 'kill' in data:
			print('[-] client Exited')
			sys.exit(0)
		elif 'get' in data:
			print('[*] client req a file')
			get_file(conn,data[4:])
		else:
			conn.send("command not found run help ".encode())
	conn.close()
	server.close()

def fileList():
	file_list=''
	for dirpath, dirname, files in os.walk(r'C:/Users/MR Robot/Desktop/nabla t3ch/python/server_files/'):
		for file in files:
			file_list=file_list + file + '\n'
		return file_list

def get_file(conn,fname):
	path=r'C:/Users/MR Robot/Desktop/nabla t3ch/python/server_files/' + fname
	if os.path.exists(path):
		f=open(path,'r')
		pak=f.read(1024)
		while pak !='':
			conn.send(pak.encode())
			pak=f.read(1024)
		conn.send("DONE".encode())
		f.close()
	else:
		conn.send("NOT_FOUND".encode())


if __name__ == '__main__':
	connect()