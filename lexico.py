import ply.lex as lex

# Palabras reservadas
words_reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'while': 'WHILE',
    'int': 'INT',
    'float': 'FLOAT',
    'string': 'STRING'
}

# Lista de tokens, incluyendo operadores lógicos y relacionales
tokens = [
    'ID', 'NUMBER', 'STRING_LITERAL',
    'LPAREN', 'RPAREN', 'PLUS', 'MINUS', 'DIVIDE', 'TIMES',
    'LBRACE', 'RBRACE', 'LBRACKET', 'RBRACKET',
    'EQUALS', 'SEMICOLON', 'LT', 'GT', 'LE', 'GE', 'COMMA',
    'LOR', 'LAND', 'EQ', 'NE'
] + list(words_reserved.values())

# Reglas para los tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_EQUALS = r'='
t_SEMICOLON = r';'
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='   # Nuevo operador menor o igual
t_GE = r'>='   # Nuevo operador mayor o igual
t_COMMA = r','
t_LOR = r'\|\|'  # OR lógico
t_LAND = r'&&'   # AND lógico
t_EQ = r'=='
t_NE = r'!='

# Reglas para números
def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Regla para strings
def t_STRING_LITERAL(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.value = t.value[1:-1]
    return t

# Regla para identificadores y palabras reservadas
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = words_reserved.get(t.value, 'ID')
    return t

# Ignorar espacios y tabulaciones
t_ignore = ' \t\n'

# Manejo de errores
def t_error(t):
    print(f"Carácter ilegal: {t.value[0]} en la posición {t.lexpos}")
    t.lexer.skip(1)

# Construir el analizador léxico
lexer = lex.lex()
