# importamos libreria time
import time
# importamos libreria GPIO
import RPi.GPIO as GPIO
#
# configuracion para los GPIO
# usaremos la identificacion BCM para los GPIO
try:
    GPIO.setmode(GPIO.BCM)

    PIN_A = 14
    PIN_B = 15
    PIN_C = 18
    PIN_D = 23
    PIN_E = 24
    PIN_F = 25
    PIN_G = 8
    PIN_DP = 7

    # desactivamos mensajes de error
    GPIO.setwarnings(False)
    # indicamos los puertos de salida GPIO
    GPIO.setup(PIN_A, GPIO.OUT)
    GPIO.setup(PIN_B, GPIO.OUT)
    GPIO.setup(PIN_C, GPIO.OUT)
    GPIO.setup(PIN_D, GPIO.OUT)
    GPIO.setup(PIN_E, GPIO.OUT)
    GPIO.setup(PIN_F, GPIO.OUT)
    GPIO.setup(PIN_G, GPIO.OUT)
    GPIO.setup(PIN_DP, GPIO.OUT)
    #
    # definimos funcion que apaga o enciende todos los
    # segmentos del display segun el parametro
    # que enviamos 0=apagar 1=encender
    def INICIALIZAR_DISPLAY(estado):
        # si enviamos 0 apagamos los segmentos
        if estado == 0:
            GPIO.output(PIN_A, False)
            GPIO.output(PIN_B, False)
            GPIO.output(PIN_C, False)
            GPIO.output(PIN_D, False)
            GPIO.output(PIN_E, False)
            GPIO.output(PIN_F, False)
            GPIO.output(PIN_G, False)
            GPIO.output(PIN_DP, False)
        else: # si enviamos 1 encendemos los segmentos
            GPIO.output(PIN_A, True)
            GPIO.output(PIN_B, True)
            GPIO.output(PIN_C, True)
            GPIO.output(PIN_D, True)
            GPIO.output(PIN_E, True)
            GPIO.output(PIN_F, True)
            GPIO.output(PIN_G, True)
            GPIO.output(PIN_DP, True)
    #
    # definimos funcion para hacer un test del display
    # enciende uno a uno los segmentos con un
    # retraso indicado por el parametro demora
    def TEST_DISPLAY(demora):
        # aparagamos todos los segmentos
        INICIALIZAR_DISPLAY(0)
        # los encendemos uno a uno
        GPIO.output(PIN_A, True)
        time.sleep(demora)
        GPIO.output(PIN_B, True)
        time.sleep(demora)
        GPIO.output(PIN_C, True)
        time.sleep(demora)
        GPIO.output(PIN_D, True)
        time.sleep(demora)
        GPIO.output(PIN_E, True)
        time.sleep(demora)
        GPIO.output(PIN_F, True)
        time.sleep(demora)
        GPIO.output(PIN_G, True)
        time.sleep(demora)
        GPIO.output(PIN_DP, True)
    #
    # definimos funcion que recibe un parametro que debe ser
    # un numero o un punto y enciende los segmentos
    # correspondientes del display
    def PRINT_DISPLAY(digito):
        INICIALIZAR_DISPLAY(0) # apagamos todos los segmentos
        # activamos los segmentos para cada numero
        if digito== "0": # numero 0
            GPIO.output(PIN_A, True) # segmento a
            GPIO.output(PIN_B, True) # segmento b
            GPIO.output(PIN_C, True) # segmento c
            GPIO.output(PIN_D, True) # segmento d
            GPIO.output(PIN_E, True) # segmento e
            GPIO.output(PIN_F, True) # segmento f
        elif digito== "1": # numero 1
            GPIO.output(PIN_B, True) # segmento b
            GPIO.output(PIN_C, True) # segmento c
        elif digito== "2": # numero 2
            GPIO.output(PIN_A, True) # segmento a
            GPIO.output(PIN_B, True) # segmento b
            GPIO.output(PIN_D, True) # segmento d
            GPIO.output(PIN_E, True) # segmento e
            GPIO.output(PIN_G, True) # segmento g
        elif digito== "3": # numero 3
            GPIO.output(PIN_A, True) # segmento a
            GPIO.output(PIN_B, True) # segmento b
            GPIO.output(PIN_C, True) # segmento c
            GPIO.output(PIN_D, True) # segmento d
            GPIO.output(PIN_G, True) # segmento g
        elif digito== "4": # numero 4
            GPIO.output(PIN_B, True) # segmento b
            GPIO.output(PIN_C, True) # segmento c
            GPIO.output(PIN_F, True) # segmento f
            GPIO.output(PIN_G, True) # segmento g
        elif digito== "5": # numero 5
            GPIO.output(PIN_A, True) # segmento a
            GPIO.output(PIN_C, True) # segmento c
            GPIO.output(PIN_D, True) # segmento d
            GPIO.output(PIN_F, True) # segmento f
            GPIO.output(PIN_G, True) # segmento g
        elif digito== "6": # numero 6
            GPIO.output(PIN_A, True) # segmento a
            GPIO.output(PIN_C, True) # segmento c
            GPIO.output(PIN_D, True) # segmento d
            GPIO.output(PIN_E, True) # segmento e
            GPIO.output(PIN_F, True) # segmento f
            GPIO.output(PIN_G, True) # segmento g
        elif digito== "7": # numero 7
            GPIO.output(PIN_A, True) # segmento a
            GPIO.output(PIN_B, True) # segmento b
            GPIO.output(PIN_C, True) # segmento c
        elif digito== "8": # numero 8
            GPIO.output(PIN_A, True) # segmento a
            GPIO.output(PIN_B, True) # segmento b
            GPIO.output(PIN_C, True) # segmento c
            GPIO.output(PIN_D, True) # segmento d
            GPIO.output(PIN_E, True) # segmento e
            GPIO.output(PIN_F, True) # segmento f
            GPIO.output(PIN_G, True) # segmento g
        elif digito== "9": # numero 9
            GPIO.output(PIN_A, True) # segmento a
            GPIO.output(PIN_B, True) # segmento b
            GPIO.output(PIN_C, True) # segmento c
            GPIO.output(PIN_D, True) # segmento d
            GPIO.output(PIN_F, True) # segmento f
            GPIO.output(PIN_G, True) # segmento g
        elif digito== ".": # DP (punto decimal)
            GPIO.output(PIN_DP, True) # segmento DP
    #
    # Codigo para ejecutar las funciones
    # con la siguiente funcion encendemos todos segmentos
    INICIALIZAR_DISPLAY(1)
    # damos un tiempo de espera
    time.sleep(0.5)
    # con la siguiente funcion apagamos todos los segmentos
    INICIALIZAR_DISPLAY(0)
    #damos un tiempo de espera
    time.sleep(0.5)
    # llamamos a la funcion que enciende los segmentos
    # uno a uno con un tiempo de espera
    TEST_DISPLAY(0.2)
    #damos un tiempo de espera de un segundo
    time.sleep(1)
    # con la siguiente funcion apagamos todos los segmentos
    INICIALIZAR_DISPLAY(0)
    # con el siguente bucle infinito podemos introducir un
    # numero o un punto y al hacer intro aparecera en el
    # display
    while (True):
        # mensaje para el usuario
        tecla=input("introduzca un numero o punto y presione Intro en el teclado: ")
        # llamamos a la funcion que ilumina los segmentos
        PRINT_DISPLAY(str(tecla))
finally: GPIO.cleanup()
