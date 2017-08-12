class Tradutor:
  def __init__(self, filename):
    self.filename = filename

  def process(self):
    with open(self.filename, "r") as f:
      lines = f.readlines()

      # Inicializo o lexico e passo as linhas do arquivo
      lexicon = Lexicon(lines)

      print lexicon.process()

class Token:
  """
    ----------------------
    Entendimento dos ID's
    ----------------------
    
    Operadores Logicos
    1: >
    2: <
    3: >=
    4: <=
    5: ==
    6: !=
    7: identificador

    Operadores aritmeticos
    8: +
    9: -
    10: /
    11: *

    Delimitadores
    12: nova linha
    13: fim de texto

    14: atribuicao
    15: constantes numericas inteiras

    Palavras reservadas
    16: #
    17: input
    18: let
    19: print
    20: goto
    21: if
    22: end

    23: numero

    24: (
    25: )

  """
  def __init__(self, token, t_type, t_line):
    self.token = token
    self.t_type = t_type
    self.t_line = t_line

class Lexicon:

  def __init__(self, lines):
    self.lines = lines
    self.lexicon_tokens = []

  def verify_expression_logical(self, token, index_line):
    if(token == '>'):
      return Token(token, 1, index_line)
    elif(token == '<'):
      return Token(token, 2, index_line)
    elif(token == '>='):
      return Token(token, 3, index_line)
    elif(token == '<='):
      return Token(token, 4, index_line)
    elif(token == '=='):
      return Token(token, 5, index_line)
    elif(token == '!='):
      return Token(token, 6, index_line)
    else:
      return None

  def verify_operator_arithmetic(self, token, index_line):
    if(token == '+'):
      return Token(token, 8, index_line)
    elif(token == '-'):
      return Token(token, 9, index_line)
    elif(token == '/'):
      return Token(token, 10, index_line)
    elif(token == '*'):
      return Token(token, 11, index_line)
    else:
      return None

  def verify_command(self, token, index_line):
    if(token == 'input'):
      return Token(token, 17, index_line)
    elif(token == 'let'):
      return Token(token, 18, index_line)
    elif(token == 'print'):
      return Token(token, 19, index_line)
    elif(token == 'goto'):
      return Token(token, 20, index_line)
    elif(token == 'if'):
      return Token(token, 21, index_line)
    elif(token == 'end'):
      return Token(token, 22, index_line)
    else:
      return None

  def verify_number(self, token, index_line):
    if(token.isdigit()):
      return Token(token, 23, index_line)
    else: 
      return None

  def verify_variable(self,token, index_line):
    if(len(token) != 1 or token.isdigit()):
      return None
    else:
      return Token(token, 7, index_line)

  def verify_bracket(self, token, index_line):
    if(token == '('):
      return Token(token, 24, index_line)
    elif(token == ')'):
      return Token(token, 25, index_line)
    else:
      return None

  def process(self):
    for i, line in enumerate(self.lines):
      tokens = line.split()
      for j, token in enumerate(tokens):
        # Verifico comando
        verify = self.verify_command(token, i)
        if(verify != None):
          self.lexicon_tokens.append(verify)

        # verifico variavel
        verify = self.verify_variable(token, i)
        if(verify != None):
          self.lexicon_tokens.append(verify)

        # verifico numero
        verify = self.verify_number(token, i)
        if(verify != None):
          self.lexicon_tokens.append(verify)

        # verifico operador
        verify = self.verify_expression_logical(token, i)
        if(verify != None):
          self.lexicon_tokens.append(verify)

        # verifico operador aritimetico
        verify = self.verify_operator_arithmetic(token, i)
        if(verify != None):
          self.lexicon_tokens.append(verify)

        # verify brackets
        verify = self.verify_bracket(token, i)
        if(verify != None):
          self.lexicon_tokens.append(verify)

    return self.lexicon_tokens

import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

print sys.argv[1]

tradutor = Tradutor(sys.argv[1])
tradutor.process()