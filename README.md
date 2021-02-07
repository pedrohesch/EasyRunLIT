# EasyRunLIT

## INF2102 - Projeto Final de Programação

**2020.2**

Disciplina do programa de pós-graduação do Departamento de Informática da PUC-Rio.

## NOTAS INICIAIS

Este projeto é uma P.O.C de interface inicial para rodar o aplicativo LIT.
Esta versão roda apenas previsões de um modelo de linguagem pré-treinado do LIT para arquivos textos "flat" do usuário


## Instalação

### Instalando ambiente virtual

Sugestão de crianção de ambiente virtual

```bash
python -m venv lit-nlp
```

### Instalando o LIT

Instalando o Language Interpretability Tool (LIT)

```bash
pip install lit-nlp
```
para maiores detalhes consultar diretamente o repositório do LIT: https://github.com/PAIR-code/lit

### Instalando as dependências

```bash
pip install -r requirements.txt
pip install streamlit
````

### Project Structure

```
├── requirements                            - Especicifa as dependências de bibliotecas.
|
├── Demo_Datas                              - Arquivo texto para teste/demonstração.
|
├── Docs                                    - Relatório e manual completo do projeto.
|
├── Sentenv                                 - Configuração de ambiente
│   ├── sentenv    .py                      - Pacote para selecão e copia de arquinos no servidor
|
├── Tests                                   - Repositório de testes.
│   └── test_flattext.py                    - Arquivo de testes das funções do pacote flattext.
│   └── test_setenv.py                      - Arquivo de testes das funções do pacote setenv.
|
├── Userclasses                             - Repositório com as classses de preparação e carga de dados.
│   └── flattext.py                         - Pacote para preparação do arquivo de texto carregado no LIT

```

### Instalando o EasyRunLIT 

Copiar/baixar a estrutura deste repositório para a raiz do ambiente virtual criado: lit-nlp
Copiar o arquivo pretrained_lm_demo2.py para a pasta ..\lit-nlp\Lib\site-packages\lit_nlp\examples\ pretrained_lm_demo2.py

## Execução

Para executar o programa:

```bash
streamlit rum easyrulit.py
```

## Relatório

Para relatório completo, inclusive manual de usuario, ler o documento do link abaixo


