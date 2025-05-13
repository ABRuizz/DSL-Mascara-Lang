from lex import lex
import sys

# 1° passo: Definindo os tokes
tokens = ("JOGADOR", "ACAO", "PERSONAGEM","FIM_COMANDO", "MODIFICADOR", "IDENTIFICADOR",
 "TRIBUNAL", "SEPARADOR", "ABRE_PARENTESES", "FECHA_PARENTESES")

# 2° passo: Definindo as linguagens regulares de cada token (regex)
t_MODIFICADOR = "new | erase"
t_JOGADOR = "j\d+" 
t_TRIBUNAL = "tribunal"
t_ACAO = "troca | \!troca | revelar | habilidade | contestar"
t_PERSONAGEM = "rei | bobo | juiz | pedinte"
t_FIM_COMANDO = "\;"
t_SEPARADOR = "\,"
t_ABRE_PARENTESES = "\("
t_FECHA_PARENTESES = "\)"


def t_MUDA_LINHA(t):
    r"\n"
    t.lexer.lineno += 1

#Esses tokens são pre-definidos e não precisam ser declarados na tupla "tokens"
t_ignore = " "
#Definir como uma função
def t_error(t):
    print(t, "não foi reconhecido!")
    sys.exit(0)

# def t_IDENTIFICADOR(t):
#     "new | erase" 
   
#     if t.value in ('new', 'erase'):
#         t.type = 'MODIFICADOR'
#     return t

def inicializaLexer(arquivo):
    # 3°passo: Abrir o código fonte
    data = open(arquivo)
    conteudo = data.read()
    print(conteudo)

    # 4°passo: Instanciar o Lexer
    lexer = lex()
    lexer.input(conteudo)
    return lexer