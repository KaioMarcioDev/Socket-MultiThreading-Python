import threading
import socket

clients = []

def main():

	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:
		server.bind(('localhost',8000))
		server.listen()

	except:
		return print('\nNçao foi possivel iniciar o servidor')


	while True:
		client, addr = server.accept()	
		clients.append(client)

		thread = threading.Thread(target=messagesTreatment, args=[client])
		thread.start()



	def messagesTreatment(client):
		while True:
			try:
				msg = client.recv(2048)	
				broadcast(msg, client)
			except:
				deleteClient(client)
				break


	def broadcast(msg, client):
		for clientItem in clients:
			if clientItem != client:
				try:
					clientItem.send(msg)
				except:
					deleteClient(deleteClient)
	
	def deleteClient(client):
		clients.remove(client)				










main()	