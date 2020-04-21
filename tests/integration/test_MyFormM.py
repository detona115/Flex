# -*- encoding: utf-8 -*-

#import pytest
#import warnings
import unittest
from unittest.mock import patch
from unittest.mock import Mock

import MyFormM

import sys 
from PyQt5.QtWidgets import QApplication

from psycopg2 import Error
import psycopg2
from queries import criarTabelaUser, criarTabelaDividas, inserirUsers, listClients, saveNewDebt

CREATE_TAB = "CREATE TABLE IF NOT EXISTS users(\
        id INT NOT NULL PRIMARY KEY,\
        name varchar(100),\
        username varchar(100),\
        email varchar(100),\
        address jsonb,\
        phone varchar(50),\
        website varchar(50),\
        company jsonb);"

CREATE_DIV = "CREATE TABLE IF NOT EXISTS debts(\
        id SERIAL,\
        iduser INT REFERENCES users(id) ON DELETE CASCADE,\
        reason varchar(150),\
        data DATE,\
        value DECIMAL,\
        PRIMARY KEY(id, iduser));"

INSERT_USER = "INSERT INTO users VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"

LIST_USERS = "SELECT\
        id, name, username, email,\
        address ->> 'city',\
        address ->> 'street',\
        address ->> 'zipcode',\
        phone FROM users;"

NEW_DEBT = "INSERT INTO debts (iduser, reason, data, value) VALUES (%s, %s, %s, %s)"

class MyFormTest(unittest.TestCase):

    def setUp(self):
        print("Criando uma instancia de MyForm em integration-- ")
        self.app = QApplication(sys.argv)
        self.cvt = MyFormM.MyForm()                               

    def test_initApp(self): # => Integração pq chama outras função do mesmo modulo na sua execução
        # Testando se a função initApp está sendo chamada         
        with patch('MyFormM.MyForm.initApp') as mocked_initApp:               
            self.cvt.initApp()
            mocked_initApp.assert_called()                   

    def test_createTables(self): # test de integração por receber param de outro modulo e chamar connection pra se conectar
        # Testando se a função recebe a query para criar a tabela user
        query = criarTabelaUser()
        mock = Mock(spec = self.cvt.createTables)
        mock(query)
        # Testando se o parametro recebido corresponde ao se espera
        mock.assert_called_with(CREATE_TAB)

        # Testando se a função recebe a query para criar a tabela vididas
        query = criarTabelaDividas()
        mock(query)
        # Testando se o parametro recebido corresponde ao que se espera
        mock.assert_called_with(CREATE_DIV)
        
    def test_storeUsers(self): # => integração pq recebe query em param
        query = inserirUsers()
        # Testando se a função storeUsers está sendo chamada
        #with self.assertRaises(AttributeError):
        #    with patch('MyFormM.MyForm.storeUsers') as mocked_users:
        #        with patch('MyFormM.requests.json') as mocked_storeUsers:                    
        #            mocked_storeUsers.side_effect = None
        #            #mocked_users.side_effect = Exception(AttributeError)
        #            self.cvt.storeUsers(query)                
        #            mocked_users.assert_called_with(query)    

        # Testando se a função recebe a query para criar a tabela user
        with self.assertRaises((AttributeError)):
            mock = Mock(spec = self.cvt.storeUsers)
            mock(query)
            # Testando se o parametro recebido corresponde ao que se espera
            mock.assert_called_with(INSERT_USER)
            # Testando se o exception AttibuteError é levantado caso a requests seja igual None  
            mock_requests = Mock(spec=MyFormM.requests.json)    
            mock_requests.side_effect = None              

    def test_listUsers(self): # => integração pq recebe query em param
        #with patch('MyFormM.MyForm.listUsers') as mocked_listUsers:
            #self.cvt.listUsers()
            #mocked_listUsers.assert_called()  
        
        query = listClients()
        mock = Mock(spec=self.cvt.listUsers)            
        mock(query)                       
        mock.assert_called_with(LIST_USERS)     

    
    def test_newDebt(self): # integração pq recebe query em param
        
        ''' não é possível fazer o patch das variáveis locais da função newDebt
            a função mock até a versão 3.8 ainda não permite essa possibilidade
            pois elas permitiriam testar se a execessões estão occorendo como deve
            o teste se limitará somente a conferir se a função tá sendo chamada 
            com o parametro esperado '''
    
        query = saveNewDebt()
        mock = Mock(self.cvt.newDebt)  
        mock(query)       
        mock.assert_called_with(NEW_DEBT)



if __name__ == "__main__":
    #unittest.main()

    suite = unittest.TestSuite()
    if len(sys.argv) == 1:
        suite = unittest.TestLoader().loadTestsFromTestCase(MyFormTest)
    else:
        for test_name in sys.argv[1:]:
            suite.addTest(MyFormTest(test_name))
    unittest.TextTestRunner(verbosity=2).run(suite)

   