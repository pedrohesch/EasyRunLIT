#app de interface para rodar o LIT

#importando os pacotes necessários
import streamlit as st
import subprocess
import os
import shutil
st.set_option('deprecation.showfileUploaderEncoding', False)
from pathlib import Path

def file_selector():
	'''
	Retorna a busca de um arquivo de texto na maquina local.
	'''
	return st.file_uploader("Carregue um arquivo texto", type=["txt"])

def test_file_selector():
	pass

def copy_file_to_lit(filename):
	'''
	Cria um arquivo de texto chamado demofile.txt na pasta de datasets do LIT e copia
	todo o conteúdo do arquivo texto selecionado para ele.
	'''
	
	f = open("./Lib/site-packages/lit_nlp/examples/datasets/demofile.txt", "w")
	f.write(str(filename.read(),"utf-8"))
	f.close()

def test_copy_file_to_lit():
	my_file = Path("./Lib/site-packages/lit_nlp/examples/datasets/demofile.txt")
	assert my_file.is_file() == True

def copy_class_to_lit(classfile):
	'''
	Copia o arquivo com a classe de preparação de dados para o servidor LIT, na pasta de datasets onde 
	se encontram os demais pacotes do gênero. 
	'''
	shutil.copyfile(classfile, './Lib/site-packages/lit_nlp/examples/datasets/userdataset.py')

def test_copy_class_to_lit():
	my_file = Path("./Lib/site-packages/lit_nlp/examples/datasets/userdataset.py")
	assert my_file.is_file() == True


