from socket import *


def cli_connect():
	cli=socket(AF_INET,SOCK_STREAM)
	cli.connect(('localhost',1112))
	print("[*] connected successfully ^_^")
	help="""\
	[*]allowed command :
		kill: terminate the connection
		show_files: show the file list
		get <file name> :get file from server
	"""

	usage="""\
	nabla t3ch >> help
	nabla t3ch >> show_files
	nabla t3ch >> get <file name>
	"""
	print(help)
	print(usage)



	while True:
		comm=input("nabla t3ch >> ")
		if 'kill' in comm:
			print("killing connection")
			cli.send(comm.encode())
			break
		elif 'help' in comm:
			print(help)
		elif 'get' in comm:
			print('[*] getting file ...')
			cli.send(comm.encode())
			recv_file(cli,comm)
		elif 'show_files' in comm:
			cli.send(comm.encode())
			comm=cli.recv(1024)
			comm=comm.decode()
			print("SERVER files are ")
			print(comm)
		elif 'usage' in comm:
			print(usage)
		else:
			print("invalid input ")
			print(help)
	cli.close()

def recv_file(conn,code):
	fname=code[4:]
	f=open(r'C:/Users/MR Robot/Desktop/nabla t3ch/python/'+fname,'w')
	while True:	
		pak=conn.recv(1024)
		pak=pak.decode()
		if 'NOT_FOUND' in pak:
			print('[*] Unable to find file  :(')
			break
		elif pak.endswith('DONE'):
			print("[*] Done Transfaring ^_^")
			break
		f.write(pak)



if __name__ == '__main__':
	cli_connect()