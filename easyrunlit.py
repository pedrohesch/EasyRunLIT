"""
Fluxo principal do programa easyrunlit.
Sobe o serviço de aplicação web via Streamlit e executa o programa.
Criado em 07 de fev 2021
@author: Pedro Schneider
@version: 1.0

"""

import streamlit as st
import subprocess
from Setenv.setenv import set_environment


def main():

	# Titulo principal da pagina
	st.title('INTERFACE PARA PRE-CARREGAMENTO DO APP LIT')

	# sub-titulo de pagina
	st.header("AREA DE CARREGAMENTO DE DADOS")
	st.markdown("---")

	# carrega o arquivo texto selecionado na variavel filename
	filename = set_environment.file_selector()

	# clicando no botão na interface, executa a função de copiar o arquivo texto
	if st.button("Copia o arquivo para o servidor LIT"):
		set_environment.copy_file_to_lit(filename)

	# sub-titulo de pagina	
	st.header("AREA DE PREPARAÇÃO DE DADOS")
	st.markdown('---')

	# cria um seletor na interface grafica, atribuindo a seleção na variável prepdata
	prepdata = st.radio("Seleciona a preparação dos dados ",['Pre-Processamento 1','Pre-Processamento 2'])

	# de acordo com a seleção do tipo de pre-processamento, carrega o pacote de classe necessário em classfile
	if prepdata == 'Pre-Processamento 1':
		st.write ('Recebe um arquivo texto e o transforma em uma lista de sentenças para o modelo')
		classfile = './Userclasses/flattext.py'

	elif prepdata == 'Pre-Processamento 2':
		st.write ('Em desenvolvimento...')

	# ao clicar no botão na interface, copia o pacote de classe escolhido e chama o LIT
	if st.button("Rodar o LIT"):
		set_environment.copy_class_to_lit(classfile)
		st.write ('Rodando...')
		st.markdown('_checar **url** na janena de comando_.')
		#subprocess.call('python -m lit_nlp.examples.pretrained_lm_demo2 --models=bert-base-uncased --port=5432')


if __name__ == '__main__':
    main()