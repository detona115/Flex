# -*- encoding: utf-8 -*-

#import pytest
#import warnings
import unittest
from unittest.mock import patch
from unittest.mock import Mock

#import PyQt5.QtWidgets
#import flex
import sys
import MyFormM

from PyQt5.QtWidgets import QApplication

from psycopg2 import Error
import psycopg2
import requests

class MyFormTest(unittest.TestCase):

    def setUp(self):
        print("Criando uma instancia de MyForm em unit -- ")
        self.app = QApplication(sys.argv)
        self.cvt = MyFormM.MyForm()    

    def test_fetchDatas(self): 
        reponse = self.cvt.fetchDatas()
        # Testando se houve conexão com a API
        self.assertEqual(200, reponse.status_code, "Conexão não sucedida ao endpoint")
        self.assertEqual(reponse.ok, True)
        
        # Testando se a API retornou os dados
        assert len(reponse.json()[0]) > 1
        # Testando se a Exception está sendo chamada no caso de AttributeError
        with self.assertRaises(AttributeError):
            with patch('MyFormM.requests.json') as mocked_get:                
                mocked_get.side_effect = None                     

    def test_call_showButton(self):
        # Testando se a função showButton está sendo chamada
        with patch('MyFormM.MyForm.showButton') as mocked_showButton:
            self.cvt.showButton()
            mocked_showButton.assert_called()
            # Testando se o groupBox inicia com False
            self.assertEqual(self.cvt.ui.groupBox_3.isChecked(), False)

    def test_connection(self):
        expected = self.cvt.connection()
        # Testando se a conexão com postgres está ativa ou aberta
        assert expected.closed == 0
        # Testando se a conexão está sendo feita com as credenciais esperadas
        assert expected.dsn == 'user=debug password=xxx dbname=flex host=172.23.0.1'
        # Testando o Except Error caso ocorra falha na conexão
        with self.assertRaises(psycopg2.Error):    
            with patch('MyFormM.MyForm.connection') as mocked_conn:              
                mocked_conn.side_effect = psycopg2.connect(host="172.23.0.1", user="debug", password="5678", database="flex")                

    def test_createDatabase(self): 
        # Testando se função createDatabase está sendo chamada
        with self.assertRaises(psycopg2.Error):
            with patch('MyFormM.MyForm.createDatabase') as mocked_createDatabase:                              
                self.cvt.createDatabase()
                mocked_createDatabase.assert_called()
                mocked_createDatabase.side_effect = psycopg2.connect(host="172.23.0.1", user="debug", password="5678",  database="postgres")     

    @patch('MyFormM.MyForm.listUserDebts')
    def test_listUserDebts(self, mock):
        self.cvt.listUserDebts()
        mock.assert_called()
        
    @patch.object(MyFormM.MyForm, 'apagarDivida')
    def test_apagarDivida(self, mock):
        self.cvt.apagarDivida()
        mock.assert_called()

    #@patch(MyFormM.MyForm, 'alterarDivida')
    def test_alterarDivida(self):
        mock = Mock(spec=self.cvt.alterarDivida)
        mock()
        mock.assert_called_with()

if __name__ == "__main__":
    #unittest.main()

    suite = unittest.TestSuite()
    if len(sys.argv) == 1:
        suite = unittest.TestLoader().loadTestsFromTestCase(MyFormTest)
    else:
        for test_name in sys.argv[1:]:
            suite.addTest(MyFormTest(test_name))
    unittest.TextTestRunner(verbosity=2).run(suite)

   