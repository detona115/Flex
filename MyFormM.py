# -*- encoding: utf-8 -*-

'''
Created on 12 de mar de 2020

@author: ANDY
'''
from flex import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5.QtCore import QDate
import requests
from requests.exceptions import ConnectionError
from requests.exceptions import InvalidURL
# import json
import psycopg2
from psycopg2.extras import Json
from psycopg2 import Error

from queries import criarTabelaUser, criarTabelaDividas, saveNewDebt, listClients, inserirUsers


class MyForm(QMainWindow):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## inicializando todos os formularios da app
        self.initApp()

        ### definindo os eventos de cada butões

        ## listar todos os clientes
        query = listClients()
        self.ui.pushButtonListAllUsers.clicked.connect(lambda: self.listUsers(query))

        ## salvar nova divida
        query2 = saveNewDebt()
        self.ui.pushButtonSalvarDebt.clicked.connect(lambda: self.newDebt(query2))

        ## listar as dividas de um determinado cliente
        query3 = None
        self.ui.pushButtonListClientDebts.clicked.connect(self.listUserDebts)

        ## deletar uma dívida de um determinado cliente
        self.ui.pushButtonExcluirDivida.clicked.connect(self.apagarDivida)

        ## alterar uma dívida
        self.ui.pushButtonAlterarDivida.clicked.connect(self.alterarDivida)

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.showButton)
        timer.start(100)
        self.showButton()

        self.show()

    ## Fim construtor

    # esta função é chamada para ativar ou não o butão excluid divida
    def showButton(self):

        if self.ui.groupBox_3.isChecked():
            self.ui.pushButtonExcluirDivida.setEnabled(False)
        else:
            self.ui.pushButtonExcluirDivida.setEnabled(True)

    ## Função que inicializa todas as opções do App
    def initApp(self):

        ## chamando a função para criar a base de dado
        self.createDatabase()

        ## criando a tabela users
        query = criarTabelaUser()
        self.createTables(query)

        ## criando a tabela dividas
        query = criarTabelaDividas()
        self.createTables(query)

        ## inserindo os dados recebidos da API na base dado local
        query = inserirUsers()
        self.storeUsers(query)

        ## configurando o formato da data e recuperando a data atual pelo sistema
        self.ui.dateEditData.setDisplayFormat("dd-MM-yyyy")
        self.ui.dateEditData.setDate(QDate.currentDate())

        ## configurando o formato da alter data e recuperando o formato data atual pelo sistema
        self.ui.dateEdit.setDisplayFormat("dd-MM-yyyy")
        self.ui.dateEdit.setDate(QDate.currentDate())

        ## colocando os nomes de todos os clientes na combobox
        cur = self.connection().cursor()
        try:
            query = "SELECT name FROM users;"
            cur.execute(query)
            rows = cur.fetchall()
            if not rows:
                raise (Error)
        except Error as errGetData:
            self.statusBar().setStyleSheet("color: red")
            self.statusBar().showMessage("Postgres server :'" + str(errGetData) + "'", 4000)

        else:
            # adicionando os nomes dos clientes na combobox Select Client
            for i in rows:
                self.ui.comboBoxClient.addItem(str(i[0]))
                self.ui.comboBoxSelectClient.addItem(str(i[0]))
        cur.close()
        self.connection().close()

    ### Função que retorna uma conexão à base de dados com
    def connection(self):
        try:
            conn = psycopg2.connect(host="172.23.0.1", user="debug", password="1234", database="flex")
            conn.autocommit = True
        except Error as errConn:
            self.statusBar().setStyleSheet("color: red")
            self.statusBar().showMessage("Postgres server :'" + str(errConn) + "'", 4000)

        else:
            return conn

    ### Função que cria a base de dados
    def createDatabase(self):
        ### função que tem por objetivo criar a base de dado se não existir
        ### e criar a tabela

        conn = psycopg2.connect(host="172.23.0.1", user="debug", password="1234", database="postgres")
        try:
            # conectando ao postgres server e criando a base de dado delivery

            conn.autocommit = True
            cur = conn.cursor()

            cur.execute("CREATE DATABASE flex;")
        except Error as errCreateDb:
            self.statusBar().setStyleSheet("color: orange")
            self.statusBar().showMessage("Database loaded successfully!", 4000)
        finally:
            pass
            cur.close()
            conn.close()

    ### Função que cria as tabelas da base de dados
    def createTables(self, query):
        cur = self.connection().cursor()
        try:
            # recuperando a conexão à base de dados
            # e criando a as tabelas                                   
            cur.execute(query)
        except Error as errCreateTab:
            self.statusBar().setStyleSheet("color: red")
            self.statusBar().showMessage("Postgres server :'" + str(errCreateTab) + "'", 4000)
        finally:
            # cur.close()
            # self.connection().close()
            pass

    ### Função que recupera os dados do Endpoint da API
    def fetchDatas(self):
        # recuperando os dados pelo link da endpoint        
        try:
            response = requests.get('https://jsonplaceholder.typicode.com/users')
        # se não puder se conectar, notificar na barra de status
        except ConnectionError as identifier:
            self.statusBar().setStyleSheet("color: red")
            self.statusBar().showMessage("Sem conexão internet", 4000)

        else:
            return response

    ### Função que salva os dados recebidos pela API na base de dados
    def storeUsers(self, query):

        cur = self.connection().cursor()
        try:
            ## recuperando os dados da API
            self.datas = self.fetchDatas().json()

            # testa se todos os dados estão sendo inseridos corretamente
            # caso ocorra um erro indica na barra de status                   
            with cur:
                for data in self.datas:
                    idx = data['id']
                    name = data['name']
                    username = data['username']
                    email = data['email']
                    address = data['address']
                    phone = data['phone']
                    website = data['website']
                    company = data['company']
                    cur.execute(query, (idx, name, username, email, Json(address), phone, website, Json(company)))

        except Error as errInsert:
            self.statusBar().setStyleSheet("color: red")
            self.statusBar().showMessage("Error inserting data! : '" + str(errInsert) + "'", 5000)
        else:
            # caso todos os dados for inseridos de forma correta, notificar na barra de status                
            self.statusBar().setStyleSheet("color: green")
            self.statusBar().showMessage("Data inserted successfully into the table!", 5000)
        finally:
            cur.close()
            self.connection().close()

    ### Tab List Users

    ## Função que lista todos os clientes da base de dados
    def listUsers(self, query):

        cur = self.connection().cursor()
        try:
            # limpando a tabela de list users
            self.ui.tableWidgetListUsers.clearContents()
            self.ui.tableWidgetListUsers.setRowCount(0)
            # solicitando ao banco de dados todas as linhas contendo dados                   
            with cur:
                cur.execute(query)
                rows = cur.fetchall()
                if rows:
                    # caso o banco de dados tenha algum dado salvo 
                    # retornar tudo e imprimir na tel
                    self.ui.tableWidgetListUsers.setRowCount(0)
                    for rowNo, x in enumerate(rows):
                        self.ui.tableWidgetListUsers.insertRow(rowNo)
                        for col, data in enumerate(x):
                            oneColumn = QTableWidgetItem(str(data))

                            self.ui.tableWidgetListUsers.setItem(rowNo, col, oneColumn)
                    self.statusBar().setStyleSheet("color: green")
                    self.statusBar().showMessage("Client List loaded successfully!", 5000)
                else:
                    # caso contrario levantar um erro e imprimir na barra de status
                    raise (ValueError)
        except Error as e:
            self.statusBar().setStyleSheet("color: red")
            self.statusBar().showMessage("Error trying to retrieve data from database!", 5000)

        except ValueError:
            self.statusBar().setStyleSheet("color: red")
            self.statusBar().showMessage("There is no clients registered into the database!", 5000)
            # print("não tem dados cadastrados na base de dados")
        finally:
            cur.close()
            self.connection().close()

    ### Tab new debt

    ## Função que cadastra uma nova divida referente 
    ## a um cliente já existente na base de dados
    def newDebt(self, query):

        # recuperando os valores do formulário
        user = self.ui.comboBoxClient.currentText()
        motivo = self.ui.lineEditMotivo.text()
        valor = self.ui.doubleSpinBoxValor.value()
        data = self.ui.dateEditData.date().toString('yyyy-MM-dd')

        cur = self.connection().cursor()
        try:

            # verificando se todos os campos do formulario foram completados
            if not user or not motivo or (valor < 0.01) or not data:
                raise (ValueError)

            cur.execute("SELECT id FROM users WHERE name = '" + user + "'")
            ids = cur.fetchone()[0]
            cur.execute(query, (ids, motivo, data, valor))
            # cur.execute("INSERT INTO debts (iduser, reason, data, value) VALUES ('"+ids+"', '"+motivo+"', '"+data+"', '"+valor+"')")
        except Error as errUser:
            self.statusBar().setStyleSheet("color: red")
            self.statusBar().showMessage("Error trying to retrieve data from database! : " + str(errUser), 4000)

        except ValueError:
            self.statusBar().setStyleSheet("color: red")
            self.statusBar().showMessage("Form incomplete or Valor < 0.01 !", 4000)
        else:
            self.ui.lineEditMotivo.clear()
            self.ui.doubleSpinBoxValor.setValue(0)
            self.statusBar().setStyleSheet("color: green")
            self.statusBar().showMessage("New Debt stored successfully into the database!", 5000)
        finally:
            cur.close()
            self.connection().close()

    ### Tab List User Debt

    ## Função que lista as dívidas de um determinado cliente
    def listUserDebts(self):

        # recuperando os valor da combobox
        user = self.ui.comboBoxSelectClient.currentText()

        cur = self.connection().cursor()
        try:
            # limpando a tabela
            self.ui.tableWidgetListUserDebt.clearContents()
            self.ui.tableWidgetListUserDebt.setRowCount(0)

            cur.execute("SELECT id FROM users WHERE name = '" + user + "'")
            ids = cur.fetchone()[0]
            cur.execute("SELECT id, reason, data, value FROM debts WHERE iduser = '" + str(ids) + "'")
            rows = cur.fetchall()
            # se o cliente não tiver dívidas, limpar a combobox e notificar na barra de status
            if not rows:
                raise (ValueError)
        except Error as errListDebt:
            self.statusBar().setStyleSheet("color: red")
            self.statusBar().showMessage("Error trying to retrieve user list debt from database! : " + str(errListDebt),
                                         4000)

        except ValueError:
            self.ui.comboBoxIdDivida.clear()
            self.statusBar().setStyleSheet("color: orange")
            self.statusBar().showMessage("The Client has no Debt!", 5000)
        else:
            self.ui.tableWidgetListUserDebt.setRowCount(0)
            for rowNo, x in enumerate(rows):
                self.ui.tableWidgetListUserDebt.insertRow(rowNo)
                for col, data in enumerate(x):
                    oneColumn = QTableWidgetItem(str(data))

                    self.ui.tableWidgetListUserDebt.setItem(rowNo, col, oneColumn)
            self.statusBar().setStyleSheet("color: green")
            self.statusBar().showMessage("Client Debt Found!", 5000)

            # Atualizando a lista dos id dívida de um determinado cliente na combobox
            user = self.ui.comboBoxSelectClient.currentText()

            # recuperando o id do atual usuario selecionado na combobox
            cur.execute("SELECT id FROM users WHERE name = '" + user + "'")
            ids = cur.fetchone()[0]

            # recuperando as dívidas do usuario em questão     
            cur.execute("SELECT id FROM debts WHERE iduser = '" + str(ids) + "'")
            rows2 = cur.fetchall()

            # se o cliente tiver dívidas, atulizar a lista na combobox
            if rows2:
                self.ui.comboBoxIdDivida.clear()
                for x in rows2:
                    self.ui.comboBoxIdDivida.addItem(str(x[0]))
        finally:
            cur.close()
            self.connection().close()

    ## Função que deleta uma dívida
    def apagarDivida(self):

        cur = self.connection().cursor()
        try:
            # recuperando o id da combobox                       
            ids = self.ui.comboBoxIdDivida.currentText()
            # se o combobox estiver sem dados 
            if ids == '':
                raise (ValueError)
            # Deletando uma dívida usando como referencia o id da dívida
            cur.execute("DELETE FROM debts WHERE id = '" + ids + "'")

        except Error as errIdDebt:
            self.statusBar().setStyleSheet("color: red")
            self.statusBar().showMessage("Error deleting data from database! : " + str(errIdDebt), 4000)

        except ValueError:
            self.statusBar().setStyleSheet("color: red")
            self.statusBar().showMessage("Any ID was provided!", 4000)
        else:
            # se a dívida for deletada, notificar na barra de status e retornar a tabela de dívidas atualizada
            self.listUserDebts()
            self.statusBar().setStyleSheet("color: green")
            self.statusBar().showMessage("Debt deleted successfully!", 5000)
        finally:
            cur.close()
            self.connection().close()

            ## Função que altera uma dívida

    def alterarDivida(self):

        # recuperando os dados do formulario
        ids = self.ui.comboBoxIdDivida.currentText()
        motivo = self.ui.lineEdit.text()
        data = self.ui.dateEdit.date().toString('yyyy-MM-dd')
        valor = self.ui.doubleSpinBox.value()

        cur = self.connection().cursor()
        try:
            # verificando se o formulario foi preenchido totalmente
            if ids == '' or not motivo or not data or (valor < 0.01):
                raise (ValueError)
        except ValueError:
            self.statusBar().setStyleSheet("color: red")
            self.statusBar().showMessage("Alter debt form incomplete or Valor < 0.01 !", 4000)
        else:
            try:
                cur.execute("UPDATE debts SET reason = '" + motivo + "', data = '" + data + "', value = '" + str(
                    valor) + "' WHERE id = '" + ids + "';")
            except Error as errUpdt:
                self.statusBar().setStyleSheet("color: red")
                self.statusBar().showMessage("Error trying to alter data : " + str(errUpdt), 4000)
            else:
                self.listUserDebts()
                self.statusBar().setStyleSheet("color: green")
                self.statusBar().showMessage("Debt updated successfully!", 5000)
        cur.close()
        self.connection().close()
