# Gramatica
import ply.lex as lex
import ply.yacc as yacc
import sys

# Bandera que indica si esta correcta la entrada
bCorrecto = True

# Tokens
tokens = [
    'MAS', 'MENOS', 'MULTI', 'DIV', 'MENOR', 'MAYOR', 'DIFERENTE', 'IGUAL', 'MENOR_IGUAL', 'MAYOR_IGUAL',
    'ASIGNACION', 'OP_Y', 'OP_O', 'RESIDUO', 'NEGACION',
    'PUNTOYCOMA', 'COMA', 'PAREN_IZQ','PAREN_DER', 'CORCHETE_IZQ', 'CORCHETE_DER',
    'LLAVE_IZQ', 'LLAVE_DER', 'ID', 'CTE_STRING', 'CTE_INT','CTE_DEC'
]

palabras_reservadas = {
    'int'   	        : 'VAR_INT',
    'dec' 	            : 'VAR_DEC',
    'boolean'           : 'VAR_BOOL',
    'string'            : 'VAR_STRING',
    'verdadero'         : 'VERDADERO',
    'falso'             : 'FALSO',
    'inicio' 	        : 'INICIO',
    'regresa'			: 'REGRESA',
    'func'              : 'FUNC',
    'void'              : 'VOID',
    'nulo'              : 'NULO',
    'si'	            : 'SI',
    'sino'	            : 'SINO',
    'mientras'          : 'MIENTRAS',
    'repetir'           : 'REPETIR',
    'colocarObjeto'     : 'COLOCAR',
    'mover'             : 'MOVER',
    'rotar'             : 'ROTAR',
    'girarDerecha'      : 'GIRAR_DER',
    'girarIzquierda'    : 'GIRAR_IZQ',
    'caminoLibre'       : 'CAMINO_LIBRE',
    'deteccion'         : 'DETECCION',
    'ocultar'           : 'OCULTAR',
    'posicion'          : 'POSICION',
    'mapaCuadricula'    : 'MAPA_CUAD',
    'recogerObjeto'     : 'RECOGER_OBJ',
    'dejarObjeto'       : 'DEJAR_OBJ',
    'saltar'            : 'SALTAR',
    'matarEnemigo'      : 'MATAR_ENEMY',
    'color'             : 'COLOR',
    'trazo'             : 'TRAZO',
    'leer'              : 'LEER',
    'escribir'          : 'ESCRIBIR',
    'mostrarValor'      : 'MOSTRAR_VALOR',
    'fin'               : 'FIN'
}

# Tokens
t_MAS = r'\+'
t_MENOS = r'\-'
t_MULTI = r'\*'
t_DIV = r'\/'
t_MENOR = r'\<'
t_MAYOR = r'\>'
t_MAYOR_IGUAL = r'\>\='
t_MENOR_IGUAL = r'\<\='
t_DIFERENTE = r'\<\>'
t_IGUAL = r'\=\='
t_ASIGNACION = r'\='
t_NEGACION = r'\!'
t_OP_Y = r'\&'
t_OP_O = r'\|'
t_RESIDUO = r'\%'
t_PUNTOYCOMA = r'\;'
t_COMA = r'\,'
t_PAREN_IZQ = r'\('
t_PAREN_DER = r'\)'
t_LLAVE_IZQ = r'\{'
t_LLAVE_DER = r'\}'
t_CORCHETE_IZQ = r'\['
t_CORCHETE_DER = r'\]'
t_CTE_STRING = r'\"(\\.|[^"])*\"|\"\"'
t_CTE_INT = r'[0-9]+'
t_CTE_DEC = r'[0-9]+\.[0-9]+'

# Tokens + palabras reservadas
tokens = tokens + list(palabras_reservadas.values())

# ID's
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = palabras_reservadas.get(t.value,'ID')
    return t

# Caracteres ignorados
t_ignore = ' \t'

# Comentarios
def t_COMENTARIO(t):
	r'\#.*'
	pass

# Comentarios
def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

# Caracteres invalidos
def t_error(t):
    global bCorrecto
    bCorrecto = False
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

# Construcion del lexer
lex.lex()



# Reglas
def p_programa(t):
    'programa : definicion INICIO LLAVE_IZQ instruccion LLAVE_DER definicion'
    print("programa")

def p_definicion(t):
    '''definicion :  definicionP
                   | empty'''
    print("definicion")
def p_definicionP(t):
    '''definicionP : funcion definicion
                    | declaracion definicion'''
    print("definicionP")

def p_instruccion(t):
    'instruccion : instruccionP'
    print("instruccion")
def p_instruccionP(t):
    '''instruccionP : declaracion PUNTOYCOMA instruccionP
    				| llamada PUNTOYCOMA instruccionP
				    | asignacion PUNTOYCOMA instruccionP
				    | condicion instruccionP
				    | ciclo instruccionP
				    | empty'''
    print("instruccion_P")

def p_funcion(t):
    'funcion : FUNC funcionP'
    print("funcion")
def p_funcionP(t):
    '''funcionP : VOID cuerpo_funcion
                | tipo cuerpo_funcion REGRESA expresion'''
    print("funcionP")
    
def p_cuerpo_funcion(t):
    'cuerpo_funcion : ID PAREN_IZQ cfP PAREN_DER LLAVE_IZQ instruccion LLAVE_DER'
    print("cuerpo_funcion")
def p_cfP(t):
    '''cfP : tipo ID cfPP
    | empty'''
    print("cfP")

def p_cfPP(t):
	'''cfPP : COMA cfPPP
    		| empty'''
	print("cfPP")

def p_cfPPP(t):
	'''cfPPP : cfP
    		| ID cfPP'''
	print("cfPPP")
    
def p_declaracion(t):
    'declaracion : tipo declaracionP'
    print("declaracion")
def p_declaracionP(t):
    'declaracionP : ID declaracionPPP declaracionPP'
    print("declaracionP")
def p_declaracionPP(t):
	'''declaracionPP : COMA declaracionP
    					| empty'''
	print("declaracionPP")
def p_declaracionPPP(t):
	'''declaracionPPP : ASIGNACION expresion
    					| declaracion_lista
    					| empty'''
	print("declaracionPPP")
    
# Se cambio la declaracion de lista
def p_declaracion_lista(t):
	'''declaracion_lista : ASIGNACION lista
    					| CORCHETE_IZQ expresion CORCHETE_DER'''
	print("declaracion_lista")
    
# Se cambio la asignacion a una lista
def p_asignacion(t):
    'asignacion : ID asignacionP ASIGNACION expresion'
    print("asignacion")
def p_asignacionP(t):
	'''asignacionP : CORCHETE_IZQ expresion CORCHETE_DER
    				| empty'''
	print("asignacionP")

def p_condicion(t):
    'condicion : SI PAREN_IZQ expresion PAREN_DER LLAVE_IZQ instruccion LLAVE_DER condicionP'
    print("condicion")
def p_condicionP(t):
	'''condicionP : SINO condicionPP
    				| empty'''
	print("condicionP")
def p_condicionPP(t):
	'''condicionPP : LLAVE_IZQ instruccion LLAVE_DER
    				| condicion'''
	print("condicionPP")

# MODIFICACION: repetir puede usar una variable entera o una constante entera
def p_ciclo(t):
	'''ciclo : MIENTRAS PAREN_IZQ expresion PAREN_DER LLAVE_IZQ instruccion LLAVE_DER
                | REPETIR repetir LLAVE_IZQ instruccion LLAVE_DER'''
	print("ciclo")
def p_repetir(t):
	'''repetir : CTE_INT
    			| ID'''
	print("repetir")

def p_llamada(t):
	'''llamada : funcionEsp
				| ID LLAVE_IZQ llamadaP LLAVE_DER'''
	print("llamada")
def p_llamadaP(t):
	'''llamadaP : expresion llamadaPP
    			| empty'''
	print("llamadaP")
def p_llamadaPP(t):
	'''llamadaPP : COMA llamadaP
    			| empty'''
	print("llamadaPPP")
    
def p_expresion(t):
	'expresion : subExp expresionP'
	print("expresion")
def p_expresionP(t):
	'''expresionP : OP_Y expresion
					| OP_O expresion
					| empty'''
	print("expresionP")
    
def p_subExp(t):
	'subExp : subExpP exp subExpPP'
	print("subExp")
def p_subExpP(t):
	'''subExpP : NEGACION
				| empty'''
	print("subExpP")
def p_subExpPP(t):
	'''subExpPP : comparador exp
    			| empty'''
	print("subExpPP")
    
def p_exp(t):
	'exp : termino expP'
	print("exp")
def p_expP(t):
	'''expP : MAS termino
    		| MENOS termino
    		| empty'''
	print("expP")

def p_termino(t):
	'termino : factor terminoP'
	print("termino")
def p_terminoP(t):
	'''terminoP : MULTI termino
    			| DIV termino
    			| RESIDUO termino
				| empty'''
	print("terminoP")
    
def p_comparador(t):
	'''comparador :   MENOR
    				| MAYOR
    				| IGUAL
    				| DIFERENTE
    				| MENOR_IGUAL
    				| MAYOR_IGUAL'''
	print("comparador")
    
def p_constante(t):
	'''constante :    NULO
    				| CTE_INT
    				| CTE_DEC
    				| CTE_STRING
    				| boolean'''
	print("constante")
    
def p_factor(t):
	'''factor : PAREN_IZQ expresion PAREN_DER
    			| opAritmetico valor'''
	print("factor")
def p_opAritmetico(t):
	'''opAritmetico : MAS
    				| MENOS
    				| empty'''
	print("opAritmetico")
    
def p_lista(t):
	'lista : CORCHETE_IZQ constante listaP CORCHETE_DER'
	print("lista")
def p_listaP(t):
	'''listaP :   COMA constante listaP
    			| empty'''
	print("listaP")

def p_valor(t):
	'''valor :    llamada
    			| ID
    			| constante'''
	print("valor")

def p_tipo(t):
	'''tipo : VAR_INT
			| VAR_DEC
			| VAR_STRING
			| VAR_BOOL'''
	if t[1] == 'int':
		print("tipo INT")
	elif t[1] == 'dec':
		print("tipo DEC")
	elif t[1] == 'string':
		print("tipo STRING")
	elif t[1] == 'boolean':
		print("tipo BOOLEAN")
    
def p_boolean(t):
	'''boolean :  VERDADERO
    			| FALSO'''
	print("boolean")
    
    
# Funciones especiales
def p_colocarObjeto(t):
	'colocarObjeto : COLOCAR PAREN_IZQ expresion COMA expresion COMA expresion PAREN_DER'
   
def p_mover(t):
	'mover : MOVER PAREN_IZQ expresion PAREN_DER'
    
def p_rotar(t):
	'rotar : ROTAR PAREN_IZQ expresion PAREN_DER'
    
def p_girarDerecha(t):
	'girarDerecha : GIRAR_DER PAREN_IZQ PAREN_DER'
    
def p_girarIzquierda(t):
	'girarIzquierda : GIRAR_IZQ PAREN_IZQ PAREN_DER'
    
def p_caminoLibre(t):
	'caminoLibre : CAMINO_LIBRE PAREN_IZQ PAREN_DER'
    
def p_deteccion(t):
	'deteccion : DETECCION PAREN_IZQ PAREN_DER'
    
def p_ocultar(t):
	'ocultar : OCULTAR PAREN_IZQ expresion PAREN_DER'
    
def p_posicion(t):
	'posicion : POSICION PAREN_IZQ expresion COMA expresion PAREN_DER'
    
def p_mapaCuadricula(t):
	'mapaCuadricula : MAPA_CUAD PAREN_IZQ expresion PAREN_DER'
    
def p_recogerObjeto(t):
	'recogerObjeto : RECOGER_OBJ PAREN_IZQ PAREN_DER'
    
def p_dejarObjeto(t):
	'dejarObjeto : DEJAR_OBJ PAREN_IZQ PAREN_DER'
    
def p_saltar(t):
	'saltar : SALTAR PAREN_IZQ PAREN_DER'
    
def p_matarEnemigo(t):
	'matarEnemigo : MATAR_ENEMY PAREN_IZQ PAREN_DER'
    
def p_color(t):
	'color : COLOR PAREN_IZQ expresion PAREN_DER'
    
def p_trazo(t):
	'trazo : TRAZO PAREN_IZQ expresion COMA expresion PAREN_DER'
    
def p_leer(t):
	'leer : LEER PAREN_IZQ leerP PAREN_DER'
def p_leerP(t):
	'''leerP : expresion
    			| empty'''
    
def p_escribir(t):
	'escribir : ESCRIBIR PAREN_IZQ expresion PAREN_DER'
    
def p_mostrarValor(t):
	'mostrarValor : MOSTRAR_VALOR PAREN_IZQ expresion PAREN_DER'
    
def p_fin(t):
	'fin : FIN PAREN_IZQ PAREN_DER'
    
def p_funcionEsp(t):
	'''funcionEsp :   colocarObjeto
    				| mover
    				| rotar
    				| girarDerecha
    				| girarIzquierda
                    | caminoLibre
                    | deteccion
                    | ocultar
                    | posicion
                    | mapaCuadricula
                    | recogerObjeto
                    | dejarObjeto
                    | saltar
                    | matarEnemigo
                    | color
                    | trazo
                    | leer
                    | escribir
                    | mostrarValor
                    | fin'''
	print("funcionEsp")
    
# Vacio (epsilon)
def p_empty(t):
    'empty :'
    print("vacio")
    pass

# Error de sintaxis 
def p_error(t):
    global bCorrecto
    bCorrecto = False
    print("Error de sintaxis en '", t.value, "' en la linea ", str(t.lineno))
    sys.exit()

# Creacion del parser
parser = yacc.yacc()

# Lectura de archivo
nombreArchivo = input("Nombre del archivo: ")
archivo = open(nombreArchivo, 'r')
contenidoArch = archivo.read()
resultado = parser.parse(contenidoArch)
print(resultado)

# Notificar si el archivo esta correcto o no
if bCorrecto == True:
    print("Archivo correcto")
else: 
    print("Archivo incorrecto")
input()
sys.exit()
