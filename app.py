# -*- coding: utf-8 -*-
from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from dbmock import clienteDados, necessidadeDados, integradorDados, projetoDados, devDados
from flask_cors import CORS

app = Flask(__name__)
db = SQLAlchemy(app)
api = Api(app)
CORS(app) # This will enable CORS for all routes

clienteDados = clienteDados()
necessidadeDados = necessidadeDados()
integradorDados = integradorDados()
projetoDados = projetoDados()
devDados = devDados()

class HelloWorld(Resource):
	def get(self):
		return {'hello': 'world'}

class cliente(Resource):
	# GET dados dele
	# POST novo cliente
	
	@app.route('/cliente/<username>', methods=['GET'])
	def showUser(username):
		return clienteDados.getCliente(username)
	
	@app.route('/cliente/', methods=['POST'])
	def newUser():
		jsonData = request.get_json()
		return clienteDados.addCliente(jsonData)

	# objeto cliente recebe uma projeto
	# -> get para ver o projeto;
	# -> post para sugerir ediçao, get para aceitar/recusar

	# pode visualizar os projetos associados a ele
	# -> get

class necessidade(Resource):
	@app.route('/necessidade/<id>', methods=['GET'])
	def showNecessidade(id):
		return necessidadeDados.getNecessidade(id)
	
	# criar objeto necessidade linkado ao cliente
	@app.route('/necessidade/', methods=['POST'])
	def newNecessidade():
		jsonData = request.get_json()
		print(jsonData)
		return necessidadeDados.addNecessidade(jsonData)

class projeto(Resource):
	# projeto é um objeto que interliga cliente, necessidade, integrador e devs
	@app.route('/projeto/<id>', methods=['GET', 'POST'])
	def projeto(id):
		if request.method == 'GET':
			return projetoDados.getProjeto(id)
		else:
			return projetoDados.editProjeto(id)

	@app.route('/projeto/', methods=['POST'])
	def newProjeto():
		## if request.form.get('necessidade') != '' and request.form.get('integrador') != '' and request.form.get('cliente') != '':
		jsonData = request.get_json()
		return projetoDados.addProjeto(jsonData)

class integrador(Resource):
	@app.route('/integrador/<id>', methods=['GET', 'POST'])
	def integrador(id):
		if request.method == 'GET':
			return integradorDados.getIntegrador(id)
		else:
			return integradorDados.editIntegrador(id)

class devs(Resource):
	@app.route('/dev/<id>', methods=['GET', 'POST'])
	def dev(id):
		if request.method == 'GET':
			return devDados.getDev(id)
		else:
			return devDados.editDev(id)


if __name__ == '__main__':
	app.run(debug=True)