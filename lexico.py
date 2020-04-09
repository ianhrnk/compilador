# -*- coding: utf-8 -*-
# ------------------------------------------------------------
 # lexico.py
 #
 # Extrator de átomos para avaliação de expressões numéricas
 # simples e operadores +,-,*,/
 # ------------------------------------------------------------
import sys
import ply.lex as lex

# Lista de palavras reservadas.
reserved = {
    'integer'   :   'INTEGER',
    'boolean'   :   'BOOLEAN',
    'true'      :   'TRUE',
    'false'     :   'FALSE',
    'read'      :   'READ',
    'write'     :   'WRITE',
    'while'     :   'WHILE',
    'if'        :   'IF',
    'else'      :   'ELSE',
    'return'    :   'RETURN'
}
 
# Lista de átomos. Essa declaração é necessária.
tokens = [
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',    
    'IDENTIFIER',
    'EQUAL',
    'DIFFERENCE',
    'LESS',
    'LESS_EQUAL',
    'GREATER',
    'GREATER_EQUAL',
    'LBRACE',
    'RBRACE',
    'LBRACKET',
    'RBRACKET',
    'COMMA',
    'ASSIGNMENT',
    'SEMICOLON',
    'OR',
    'AND',
    'EXCLAMATION',
    'INTERROGATION',
    'COLON',
    'SUMEQUALS',
    'MINUSEQUALS',
    'TIMESEQUALS',
    'DIVIDEEQUALS',
    'MOD',
] + list(reserved.values())
 
# Expressões regulares para reconhecimento de átomos simples
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_ASSIGNMENT = '='

t_ignore  = ' \t' # Cadeia que contem carcateres ignorados (espacos e tabulações)

t_LPAREN  = r'\('
t_RPAREN  = r'\)'

t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z_0-9]*' # Se nn tiver limite de caracteres.

t_EQUAL = '=='
t_DIFFERENCE = '!='
t_LESS = '<'
t_LESS_EQUAL = '<='
t_GREATER = '>'
t_GREATER_EQUAL = '>='

t_LBRACE = '{'
t_RBRACE = '}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'

t_COMMA = ','
t_SEMICOLON = ';'
t_OR = r'\|\|'
t_AND = r'&&'
t_EXCLAMATION = r'!'
t_INTERROGATION = r'\?'
t_COLON = r':'

t_SUMEQUALS = r'\+='
t_MINUSEQUALS = r'-='
t_TIMESEQUALS = r'\*='
t_DIVIDEEQUALS = r'/'
t_MOD = r'%'

'''
# Expressões regulares para reconhecimento de palvras reservadas
t_INT       =      r'int'
t_BOOL      =      r'bool'
t_TRUE      =      r'true'
t_FALSE     =      r'false'
t_READ      =      r'read'
t_WRITE     =      r'write'
'''
 
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

# Expressão regular para reconhecimento de palavras reservadas
def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in reserved:
        t.type = reserved[t.value]
    else:
        t.type = tokens[7]
    return t

# Regra para ignorar comentários de linha
def t_COMMEN_MONOLINE(t):
    r'//.*'
    pass

# Define uma regra para controle do numero de linhas
def t_newline(t):
     r'\n+'
     t.lexer.lineno += len(t.value)
  
# Regra para manipulação de erros
def t_error(t):
     print(t.lineno,": Illegal character '%s'" % t.value[0])
     t.lexer.skip(1)

def main():

    lexer = lex.lex() # Constroi o analisador lexico

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
        print ('Line: %d' % tok.lineno, tok.type, tok.value)
        
main()
