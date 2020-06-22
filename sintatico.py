import ply.yacc as yacc
import lexico

tokens = lexico.tokens # Token list

def p_program(p):
    'program : function'
    p[0] = p[1]

def p_function(p):
    'function : id_void IDENTIFIER formal_parameters block'
    p[0] = (p[1], p[3], p[4])

def p_id_void(p):
    '''id_void : IDENTIFIER 
               | VOID'''
    pass

def p_block(p):
    'block : labels_opt variables_opt functions_opt body'
    p[0] = (p[1], p[2], p[3], p[4])

def p_labels_opt(p):
    '''labels_opt : labels 
                  | empty'''
    p[0] = p[1]

def p_variables_opt(p):
    '''variables_opt : variables 
                     | empty'''
    p[0] = p[1]

def p_functions_opt(p):
    '''functions_opt : functions
                     | empty'''
    p[0] = p[1]

def p_labels(p):
    'labels : LABELS identifier_list SEMICOLON'
    p[0] = p[2]

def p_variables(p):
    'variables : VARS identifier_list COLON type SEMICOLON variables_rep'
    p[0] = (p[2], p[4], p[6])

def p_variables_rep(p):
    '''variables_rep : identifier_list COLON type SEMICOLON variables_rep
                     | empty'''
    if (len(p) == 6):
        p[0] = (p[1], p[3], p[5])
    else:
        p[0] = p[1]

def p_functions(p):
    'functions : FUNCTIONS function functions_rep'
    p[0] = (p[2], p[3])

def p_functions_rep(p):
    '''functions_rep : function functions_rep
                     | empty'''
    if (len(p) == 3):
        p[0] = (p[1], p[2])
    else:
        p[0] = p[1]

def p_body(p):
    'body : LBRACE statement_rep RBRACE'
    p[0] = p[2]

def p_statement_rep(p):
    '''statement_rep : statement statement_rep
                     | empty'''
    if (len(p) == 3):
        p[0] = (p[1], p[2])
    else:
        p[0] = p[1]

def p_type(p):
    'type : IDENTIFIER'
    pass

def p_formal_parameters(p):
    '''formal_parameters : LPAREN formal_parameter formal_parameters_rep RPAREN
                         | LPAREN RPAREN'''
    if (len(p) == 5):
        p[0] = (p[2], p[3])
    else:
        pass

def p_formal_parameters_rep(p):
    '''formal_parameters_rep : SEMICOLON formal_parameter formal_parameters_rep
                             | empty'''
    if (len(p) == 4):
        p[0] = (p[2], p[3])
    else:
        p[0] = p[1]

def p_formal_parameter(p):
    'formal_parameter : expression_parameter'
    p[0] = p[1]

def p_expression_parameter(p):
    '''expression_parameter : VAR identifier_list COLON IDENTIFIER
                            | identifier_list COLON IDENTIFIER'''
    if (len(p) == 5):
        p[0] = p[2]
    else:
        p[0] = p[1]

def p_statement(p):
    '''statement : IDENTIFIER COLON unlabeled_statement
                 | unlabeled_statement
                 | compound'''
    if (len(p) == 2):
        p[0] = p[1]
    else:
        p[0] = p[3]

def p_variable(p):
    'variable : IDENTIFIER'
    pass

def p_unlabeled_statement(p):
    '''unlabeled_statement : assignment
                           | function_call_statement
                           | goto
                           | return
                           | conditional
                           | repetitive
                           | empty_statement'''
    p[0] = p[1]

def p_assignment(p):
    'assignment : variable ASSIGN expression SEMICOLON'
    p[0] = (p[1], p[3])

def p_function_call_statement(p):
    'function_call_statement : function_call SEMICOLON'
    p[0] = p[1]

def p_goto(p):
    'goto : GOTO IDENTIFIER SEMICOLON'
    pass

def p_return(p):
    '''return : RETURN expression SEMICOLON
              | RETURN SEMICOLON'''
    if (len(p) == 4):
        p[0] = p[2]
    else:
        pass

def p_compound(p):
    'compound : LBRACE unlabeled_statement unlabeled_statement_rep RBRACE'
    p[0] = (p[2], p[3])

def p_unlabeled_statement_rep(p):
    '''unlabeled_statement_rep : unlabeled_statement unlabeled_statement_rep
                               | empty'''
    if (len(p) == 3):
        p[0] = (p[1], p[2])
    else:
        p[0] = p[1]

def p_conditional(p):
    '''conditional : IF LPAREN expression RPAREN compound ELSE compound
                   | IF LPAREN expression RPAREN compound'''
    if (len(p) == 8):
        p[0] = (p[3], p[5], p[7])
    else:
        p[0] = (p[3], p[5])

def p_repetitive(p):
    'repetitive : WHILE LPAREN expression RPAREN compound'
    p[0] = (p[3], p[5])

def p_empty_statement(p):
    'empty_statement : SEMICOLON'
    pass

def p_expression(p):
    '''expression : simple_expression
                  | simple_expression relational_operator simple_expression'''
    if (len(p) == 2):
        p[0] = p[1]
    else:
        p[0] = (p[1], p[2], p[3])

def p_relational_operator(p):
    '''relational_operator : EQUAL
                           | DIFFERENT
                           | LESS
                           | LESS_EQUAL
                           | GREATER
                           | GREATER_EQUAL'''
    pass

def p_simple_expression(p):
    '''simple_expression : PLUS term simple_expression_rep
                         | MINUS term simple_expression_rep
                         | term simple_expression_rep'''
    if (len(p) == 4):
        p[0] = (p[2], p[3])
    else:
        p[0] = (p[1], p[2])

def p_simple_expression_rep(p):
    '''simple_expression_rep : additive_operator term simple_expression_rep
                             | empty'''
    if (len(p) == 4):
        p[0] = (p[1], p[2], p[3])
    else:
        p[0] = p[1]

def p_additive_operator(p):
    '''additive_operator : PLUS
                         | MINUS
                         | OR'''
    pass

def p_term(p):
    '''term : factor term_rep'''
    p[0] = (p[1], p[2])

def p_term_rep(p):
    '''term_rep : multiplicative_operator factor term_rep
                | empty'''
    if (len(p) == 4):
        p[0] = (p[1], p[2], p[3])
    else:
        p[0] = p[1]

def p_multiplicative_operator(p):
    '''multiplicative_operator : TIMES
                               | DIVIDE
                               | AND'''
    pass

def p_factor(p):
    '''factor : variable
              | INTEGER_NUMBER
              | function_call
              | LPAREN expression RPAREN
              | NOT factor'''
    if (len(p) == 4 or len(p) == 3):
        p[0] = p[2]
    elif (p[1] == 'variable' or p[1] == 'function_call'):
        p[0] = p[1]
    else:
        pass

def p_function_call(p):
    'function_call : IDENTIFIER LPAREN expression_list RPAREN'
    p[0] = p[3]

def p_identifier_list(p):
    'identifier_list : IDENTIFIER identifier_rep'
    p[0] = p[2]

def p_identifier_rep(p):
    '''identifier_rep : COMMA IDENTIFIER identifier_rep
                      | empty'''
    if (len(p) == 4):
        p[0] = p[3]
    else:
        p[0] = p[1]

def p_expression_list(p):
    '''expression_list : expression expression_rep
                       | empty'''
    if (len(p) == 3):
        p[0] = (p[1], p[2])
    else:
        p[0] = p[1]        

def p_expression_rep(p):
    '''expression_rep : COMMA expression expression_rep
                      | empty'''
    if (len(p) == 4):
        p[0] = (p[2], p[3])
    else:
        p[0] = p[1]

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
        print("Syntax error at token", p.type)
    else:
        print("Syntax error at EOF")

def main():
    yacc.yacc() # Build the parser

    # Abre o arquivo de entrada e faz a leitura do texto
    try:
        ref_arquivo = open("teste.txt","r")
        dados = ref_arquivo.read()
        ref_arquivo.close()
    except Exception:
        print("Arquivo não encontrado")
        return
    yacc.parse(dados)

main()
