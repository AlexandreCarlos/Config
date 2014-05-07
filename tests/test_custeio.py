#!/usr/bin/env python
# -*- coding: utf-8 -*-

#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function, unicode_literals)
# from future import standard_library
# from future.builtins.disabled import apply, chr, cmp, coerce, execfile, file, input, long, raw_input, reduce, reload, \
#     unicode, xrange, StandardError
# from future.builtins.iterators import range, map, zip, filter
# from future.builtins import ascii, chr, hex, input, isinstance, oct, open, int, str, bytes
import pytest

from app import app, db

__author__ = 'alexandre'

# content of test_sample.py
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4


class Test_Config(object):
    """
        No ficheiro de configuração o Alex vai identificar os ficheiros Excel e as folhas onde estão os dados:
    """

    def test_config_exists(self):
        """
            Verifica que tem configuração ativa
        """
        assert app.config.__len__() > 0

    def test_lun_file_config(self):
        print ("# 1. Espaço de cada LUN por servidor físico;")
        assert app.config["LUN_EXCEL"] == r"/home/alexandre/Documentos/Dropbox/Gestão/DOIIC/Custeio 2013/SAN_Custeio-2013_ISA.xlsx"
        assert app.config["LUN_WKS"] == "TotaisFamilia"

    def test_bd_file_config(self):
        print ("# 2. Espaço ocupado pelas Bases de Dados relacionais de cada Aplicação, por instância de SQL;")
        assert app.config["BD_EXCEL"] == r"/home/alexandre/Documentos/Dropbox/Gestão/DOIIC/Custeio 2013" \
                                         r"/Espaço_projectos_03_01_2014.xlsx"
        assert app.config["BD_WKS"] == "Projectos"

    def test_owner_file_config(self):
        print ("# 3. Identificação do Proprietário de cada Aplicação;")
        assert app.config["OWNER_EXCEL"] == r"/home/alexandre/Documentos/Dropbox/Gestão/DOIIC/Custeio 2013" \
                                         r"/Espaço_projectos_03_01_2014.xlsx"
        assert app.config["OWNER_WKS"] == "ProprietáriosSI"

    def test_sqlite_bd_config(self):
        print ("# 4. Base de Dados SQLite")
        assert app.config["SQLALCHEMY_DATABASE_URI"] == "sqlite:///custeio.db"

    def test_custeio_file_config(self):
        print ("# 5. Ficheiro de Excel com o custeio, e a nominação das folhas com o custeio por Aplicação e por Departamento.")
        assert app.config["COSTEIO_EXCEL"] == r"/home/alexandre/Documentos/Dropbox/Gestão/DOIIC/Custeio 2013/Custeio_2013.xlsx"
        assert app.config["COSTEIO_SI_WKS"] == "Custeio_SI"
        assert app.config["COSTEIO_OWNER_WKS"] == "Custeio_Proprietários"

"""



Identificação das instâncias que são Analíticas, Relacionais, SAP,  SharePoint e Transversais
Relacionar as instâncias e os servidores.
Executando o processo "carrega_LUN.py", define a tabela "Lun" na base de dados e carrega a informação obtida do respectivo ficheiro de Excel (item 1).
Executando o processo "carrega_BD.py", define a tabela "BaseDados" na base de dados e carrega a informação obtida do respectivo ficheiro de Excel (item 2).
Executando o processo "carrega_Donos.py", define a tabela "Proprietário" na base de dados e carrega a informação obtida do respectivo ficheiro de Excel (item 3).
Executando o processo "faz_custeio.py", define a tabela "Custeio" na base de dados a partir dos seguintes cálculos:
 Proporção percentual por aplicação / instância de SQL
Calcular o total do espaço das LUNs por servidor (instância)
Distribuir o total do espaço das LUNs proporcionalmente pelas aplicações dessa instância (servidor) e guarda na tabela
Falta tratar os casos especiais (SAP,  Sybase, Dados Transversais e Servidores não BD)
SAP
É associado a um "departamento" SAP
Sybase
Instâncias de uma única aplicação, à respectiva aplicação
Instâncias multi - aplicacionais o espaço é agregado à instância relacional (SRDN2\SRDN2)
Dados Transversais
É associado ao departamento DOI
Servidores não BD
O espaço é agregado à instância relacional (SRDN2\SRDN2)
Executando o processo "report_custeio.py", define o respectivo ficheiro de Excel (item 5) e cria folha com a distribuição por aplicação do espaço em disco total, bem como a folha com o espaço em disco agregado por departamento.

"""

