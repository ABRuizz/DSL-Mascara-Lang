from lexer import inicializaLexer
import sys

lexer = inicializaLexer("main.cpp")

lookAhead = lexer.token() #Inicializando o lookAhead - sempre olha o próximo token

def match(esperado):
    global lookAhead
    if lookAhead != None and esperado == lookAhead.type:
        lookAhead = lexer.token() #continua o processo
        return

    print("Erro sintático na linha ", lookAhead.lineno, " Esperado ", esperado, " Lido ", lookAhead)
    sys.exit(1)

#todo não terminal vira um método!

def listaVar(tipo):
    if lookAhead == None:
        return
    if lookAhead.type == "FIM_COMANDO":
        match("FIM_COMANDO") #valida e chama o próximo token
        declaracao()
    elif lookAhead.type == "ABRE_PARENTESES":
        match("ABRE_PARENTESES")
        listaVar(tipo)
    elif lookAhead.type == "FECHA_PARENTESES":
        match("FECHA_PARENTESES")
        listaVar(tipo)
    elif lookAhead.type == "PERSONAGEM":
        match("PERSONAGEM")
        listaVar(tipo)
    elif lookAhead.type == "JOGADOR":
        match("JOGADOR")
        listaVar(tipo)
    elif lookAhead.type == "SEPARADOR":
        match("SEPARADOR")
        listaVar(tipo)


def declaracao():
    global lookAhead
    if lookAhead == None:
        return
        
    if lookAhead.type == "MODIFICADOR":
        tipo = lookAhead.value
        match("MODIFICADOR")
        match("JOGADOR")
        listaVar(tipo)

    elif lookAhead.type == "JOGADOR":
        tipo = lookAhead.value #devo buscar as variáveis de interesse antes do match (pq atualiza o token)
        match("JOGADOR")
        match("ACAO")
        listaVar(tipo)

def corpo():
    declaracao()

def programa():
    corpo()

programa()
print("Sintaticamente correto!")