#classe de preparação do ambiemte, escolhendo e copiando os arquivos e pacotes necessários

# importando os pacotes necessários
import streamlit as st
import subprocess
import os
import shutil
st.set_option('deprecation.showfileUploaderEncoding', False)

class set_environment():

	def file_selector():
		'''
		Retorna a busca de um arquivo de texto na maquina local.
		'''
		return st.file_uploader("Carregue um arquivo texto", type=["txt"])

	def copy_file_to_lit(filename):
		'''
		Cria um arquivo de texto chamado demofile.txt na pasta de datasets do LIT e copia
		todo o conteúdo do arquivo texto selecionado para ele.
		'''
	
		f = open("./Lib/site-packages/lit_nlp/examples/datasets/demofile.txt", "w")
		f.write(str(filename.read(),"utf-8"))
		f.close()

	def copy_class_to_lit(classfile):
		'''
		Copia o arquivo com a classe de preparação de dados para o servidor LIT, na pasta de datasets onde 
		se encontram os demais pacotes do gênero. 
		'''
		shutil.copyfile(classfile, './Lib/site-packages/lit_nlp/examples/datasets/userdataset.py')
