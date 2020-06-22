# ------------------------------------------------------------
 # lexico.py
 #
 # Extrator de átomos da linguagem SL
 # Alunos: Ian Haranaka e Adriano Rodrigues
 # ------------------------------------------------------------
import ply.lex as lex

# Palavras-chave da linguagem
keywords = {
    'void'      :   'VOID',
    'while'     :   'WHILE',
    'if'        :   'IF',
    'else'      :   'ELSE',
    'return'    :   'RETURN',
    'var'       :   'VAR',
    'labels'    :   'LABELS',
    'vars'      :   'VARS',
    'functions' :   'FUNCTIONS',
    'goto'      :   'GOTO'
}

# Identificadores predefinidos
reserved = {
    'integer'   :   'INTEGER',
    'boolean'   :   'BOOLEAN',
    'true'      :   'TRUE',
    'false'     :   'FALSE',
    'read'      :   'READ',
    'write'     :   'WRITE'
}
 
# Lista de átomos. Essa declaração é necessária.
tokens = [
    'ASSIGN',
    'INTEGER_NUMBER',
    'IDENTIFIER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'AND',
    'OR',
    'NOT',
    'EQUAL',
    'DIFFERENT',
    'LESS',
    'LESS_EQUAL',
    'GREATER',
    'GREATER_EQUAL',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'COMMA',
    'COLON',
    'SEMICOLON'
] + list(keywords.values())
 
# Expressões regulares para reconhecimento de átomos simples
t_ASSIGN  = r'\='
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'

t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'

t_EQUAL = '=='
t_DIFFERENT = '!='
t_LESS = '<'
t_LESS_EQUAL = '<='
t_GREATER = '>'
t_GREATER_EQUAL = '>='

t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACE = '{'
t_RBRACE = '}'

t_COMMA = ','
t_COLON = r':'
t_SEMICOLON = ';'
t_ignore  = ' \t' # Cadeia que contem caracteres ignorados (espacos e tabulacao)

# Uma expressão regular para reconhecimento de números inteiros
def t_INTEGER_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)    
    except ValueError:
        print ("Linha %d: O número %s é muito grande!" % (t.lineno,t.value))
        t.value = 0
    return t

# Reconhecimento de identificadores e palavras-chaves
def t_IDENTIFIER(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    if t.value in keywords:
        t.type = keywords[t.value]
    else:
        t.type = 'IDENTIFIER'
    return t

# Regra para ignorar comentários de linha
def t_COMMENT_MONOLINE(t):
    r'//.*'
    pass

# Regra para ignorar comentários de bloco
def t_COMMENT_MULTLINE(t):
    r'(/\*(.|\n)*?\*/)'
    pass

# Define uma regra para controle do numero de linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
  
# Regra para manipulação de erros
def t_error(t):
    print(t.lineno,": Caractere ilegal! '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex() # Constroi o analisador lexico

def main():
    lexer = lex.lex() # Constroi o analisador lexico

    try:
        ref_arquivo = open("teste.txt","r")
        dados = ref_arquivo.read()
        ref_arquivo.close()
    except Exception:
        print("Arquivo não encontrado")
        return
 
    print(dados) # Imprime os dados lidos (para simples conferencia

    # Chama o analisador, passando os dados como entrada
    lexer.input(dados)

    # Extrai os tokens
    while True:
        tok = lexer.token()
        if not tok: 
            break      # Final de arquivo
        print (tok.lineno, ":", tok.type, "\t", tok.value)

#main()