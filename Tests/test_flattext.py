"""
Classe para preparação do arquivo de texto carregado no LIT
Herda classe Dataset do LIT
Criado em 07 de fev 2021
@author: Pedro Schneider
@version: 1.0

"""
# pacote que prepara o arquivo de texto carregado no LIT

from lit_nlp.api import dataset as lit_dataset
from lit_nlp.api import types as lit_types

class DemoData(lit_dataset.Dataset):
  """Load sentences from a flat text file."""

  def __init__(self):
    """ Load demofile and convert it to a list of sentences """
    path = "./Lib/site-packages/lit_nlp/examples/datasets/demofile.txt"
    self._examples = []
    with open(path) as fd:
      for i, line in enumerate(fd):
        line = line.strip()
        if line:  # skip blank lines, these are usually document breaks
            self._examples.append({'text': line})

def test_load_init():
  """ Load demofile and convert it to a list of sentences """
  path = "./Lib/site-packages/lit_nlp/examples/datasets/demofile.txt"
  examples = []
  with open(path) as fd:
    for i, line in enumerate(fd):
      line = line.strip()
      if line:  # skip blank lines, these are usually document breaks
          examples.append({'text': line})
  assert type(examples) == list

  def spec(self) -> lit_types.Spec:
    """Should match MLM's input_spec()."""
    return {'text': lit_types.TextSegment()}

