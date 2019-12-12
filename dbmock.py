import json

class clienteDados:
	def __init__(self):
		self.clientes = {1:{"username":"felipe", "necessidadeIDs":[1], "projetoIDs":[1]}}
	
	def getCliente(self, id):
		if id=='all':
			return str(self.clientes)
		return str(self.clientes[int(id)])

	def addCliente(self, data):
		self.clientes.update({(len(self.clientes)+1): data})
		return str(self.clientes)
    # GET dados dele
	# POST novo cliente

	# objeto cliente recebe uma projeto
	# -> get para ver o projeto;
	# -> post para sugerir ediçao, get para aceitar/recusar

	# pode visualizar os projetos associados a ele
	# -> get
    
class necessidadeDados:
	def __init__(self):
		self.necessidades = {1:{"clienteID":1, "projetoIDs":1, "descricao": "App para vender bolos"}}

	def getNecessidade(self, id):
		if id=='all':
    			return str(self.necessidades)
		return str(self.necessidades[int(id)])

	def addNecessidade(self, data):
		self.necessidades.update({(len(self.necessidades)+1): data})
	# criar objeto necessidade linkado ao cliente
	# -> é um POST (param: cliente), cria uma necessidade para esse cliente
	
	# GET dados dela
class projetoDados:
	def __init__(self):
		self.projetos = {1:{"clienteId":1, "necessidadeIDs":1, "devIDs":[1]}}

	def addProjeto(self, id):
		self.projetos.update({(len(self.projetos)+1): id})

	def editProjeto(self, id):
		None

	def getProjeto(self, id):
		if id=='all':
    			return str(self.projetos)
		return str(self.projetos[int(id)])
	# -> get para ver o projeto;
	
	# Cliente pode dar um POST para sugerir ediçao
	# ou um GET para aceitar/recusar

	# projeto é um objeto que interliga cliente, necessidade, integrador e devs
	# -> post para criar um novo projeto
	# -> post para colocar novos devs?

	# possui um status
	# -> post ou put para alterar isso

	# POST para receber uma nota

class integradorDados:
	def __init__(self):
		self.integradores = {1:{"projetoIDs":[1]}}

	def getIntegrador(self, id):
		if id=='all':
			return str(self.integradores)
		return str(self.integradores[int(id)])

	def editIntegrador(self, data):
		None
	# GET dados dele
	# POST para receber uma nota
	# GET para aceitar uma necessidade (criar um projeto)

class devDados:
	def __init__(self):
		self.dev = {1:{"projetoIDs":[1]}}

	def addDev(self, id):
		self.dev.update({(len(self.dev)+1): id})

	def getDev(self, id):
		if id=='all':
			return str(self.dev)
		return str(self.dev[int(id)])

	# GET dados dele
	# POST para associar a um projeto?