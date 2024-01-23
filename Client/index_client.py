import threading
import socket

def main():

	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:
		client.connect(('localhost', 000))

	except:
		return print('\nNão foi possivel se conectar o servidor')


		username = input('Usuario>')
		print('\nConectado')

		thread1 = threading.Thread(target=receiveMessages, args=[client])
		thread2 = threading.Thread(target=sendMessage, args=[client, username])

		thread1.start()
		thread2.start()


	def receiveMessages(client):
		while True:
			try:
				msg = client.recv(2048).decode('utf-8')
				print(msg+'\n')
			except:
				print('\nNão foi possivel permaner conectdo ao servidor')
				print('Pressione Enter para continuar')
				client.close()
				break	
	def sendMessage(client, username):		
		while True:			
			try:			
				msg = input('\n')
				client.send(f'<{username}>{msg}'.encode('utf-8'))			
			except:				
			 return


	main()