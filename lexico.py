# ------------------------------------------------------------
# lexico.py
#
# Extrator de átomos para avaliação de expressões numéricas
# simples e operadores +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

# Lista de átomos. Essa declaração é necessária.
tokens = (
  'NUMBER',
  'PLUS',
  'MINUS',
  'TIMES',
  'DIVIDE',
  'LPAREN',
  'RPAREN',
)

# Expressões regulares para reconhecimento de átomos simples
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_ignore  = ' \t' # Cadeia que contem carcateres ignorados (espacos and tabulacao)



# Uma expressão regular para reconhecimento de números
# já exige código adicional de tratamento
def t_NUMBER(t):
  r'\d+'
  try:
    t.value = int(t.value)
  except ValueError:
    print ("Line %d: Number %s is too large!" % (t.lineno,t.value))
    t.value = 0
  return t

# Define uma regra para controle do numero de linhas
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

# Regra para manipulação de erros
def t_error(t):
  print(t.lineno,": Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)

def main():

  lexer = lex.lex() # Controi o analisador lexico

  # Abre o arquivo de entrada e faz a leitura do texto
  ref_arquivo = open("teste.txt","r")
  dados = ref_arquivo.read()
  ref_arquivo.close()

  print (dados) # Imprime os dados lidos (para simples conferencia

  # Chama o analisador, passando os dados como entrada
  lexer.input(dados)

  # Extrai os tokens
  while True:
    tok = lexer.token()
    if not tok:
      break      # Final de arquivo
    print (tok.lineno, ":", tok.type, "\t", tok.value)

main()
