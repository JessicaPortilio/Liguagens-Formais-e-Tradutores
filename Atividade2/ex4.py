import ply.lex as lex

tokens = [
    'PROGRAM_NAME',
    'HELP',
    'VERSION',
    'OPTIMIZE',
    'OUTPUT_FILE',
    'DIRECTORY',
    'NUMBER'
]

def t_PROGRAM_NAME(t):
    r'\b[a-zA-Z0-9]{1,8}\.exe\b'
    return t

def t_HELP(t):
    r'(-h|--help)'
    return t

def t_VERSION(t):
    r'(-v|--version)'
    return t

def t_OPTIMIZE(t):
    r'-O\s[0-7]'
    return t

def t_OUTPUT_FILE(t):
    r'-o\s[a-zA-Z0-9]{1,8}\.txt'
    return t

def t_DIRECTORY(t):
    r'-I\s/([a-zA-Z0-9]{1,8}/)*[a-zA-Z0-9]{1,8}'
    return t

def t_NUMBER(t):
    r'\b[0-7]\b'
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def parse_arguments(data):
    lexer.input(data)

    program_name = None
    help = False
    version = False
    optimize = None
    output_file = None
    directories = []

    while True:
        tok = lexer.token()
        if not tok:
            break
        if tok.type == 'PROGRAM_NAME':
            program_name = tok.value
        elif tok.type == 'HELP':
            help = True
        elif tok.type == 'VERSION':
            version = True
        elif tok.type == 'OPTIMIZE':
            optimize = int(tok.value.split()[-1])
        elif tok.type == 'OUTPUT_FILE':
            output_file = tok.value.split()[-1]
        elif tok.type == 'DIRECTORY':
            directories.append(tok.value.split()[-1])

    return {
        'program_name': program_name,
        'help': help,
        'version': version,
        'optimize': optimize,
        'output_file': output_file,
        'directories': directories
    }

data = "word zerosete.exe -h -O 7 -o stdout.txt -I /home/ -I /usr/"
result = parse_arguments(data)

print("Programa =", result)
