class clienteDados:
	def __init__(self):
		self.clientes = {1:{"username":"felipe", "necessidadeIDs":[1], "projetoIDs":[1]}}
	
	def getCliente(self, username):
		return str(self.clientes)

	def addCliente(self, data):
		self.clientes.update({(len(self.clientes)+1): data})
    # GET dados dele
	# POST novo cliente

	# objeto cliente recebe uma projeto
	# -> get para ver o projeto;
	# -> post para sugerir ediçao, get para aceitar/recusar

	# pode visualizar os projetos associados a ele
	# -> get
    
class necessidadeDados:
	def getNecessidade(self, id):
		return 'getNecessidade'

	def addNecessidade(self, data):
		None
	# criar objeto necessidade linkado ao cliente
	# -> é um POST (param: cliente), cria uma necessidade para esse cliente
	
	# GET dados dela
class projetoDados:
	def getProjeto(self, id):
		return 'getProjeto'

	def editProjeto(self, id):
		None

	def addProjeto(self, data):
		None
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
	def getIntegrador(self, id):
		return 'getIntegrador'

	def editIntegrador(self, data):
		None
	# GET dados dele
	# POST para receber uma nota
	# GET para aceitar uma necessidade (criar um projeto)

class devDados:
	def getDev(self, id):
		return 'getDev'

	def editDev(self, data):
		None

	# GET dados dele
	# POST para associar a um projeto?