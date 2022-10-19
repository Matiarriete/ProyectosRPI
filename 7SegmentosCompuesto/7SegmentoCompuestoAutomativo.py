# importamos libreria time
import time
# importamos libreria GPIO
import RPi.GPIO as GPIO
#
# configuracion para los GPIO
# usaremos la identificacion BCM para los GPIO
try:
    GPIO.setmode(GPIO.BCM)

    contador = 0
    promedio = 0
    PIN_A = 14
    PIN_B = 15
    PIN_C = 18
    PIN_D = 23
    PIN_E = 24
    PIN_F = 25
    PIN_G = 8
    PIN_DIG1 = 7
    PIN_DIG2 = 12

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
    GPIO.setup(PIN_DIG1, GPIO.OUT)
    GPIO.setup(PIN_DIG2, GPIO.OUT)
    #
    # definimos funcion que apaga o enciende todos los
    # segmentos del display segun el parametro
    # que enviamos 0=apagar 1=encender
    def INICIALIZAR_DISPLAY():
        # si enviamos 0 apagamos los segmentos
	GPIO.output(PIN_A, False)
        GPIO.output(PIN_B, False)
        GPIO.output(PIN_C, False)
        GPIO.output(PIN_D, False)
        GPIO.output(PIN_E, False)
        GPIO.output(PIN_F, False)
        GPIO.output(PIN_G, False)
        
    def PRINT_DISPLAY(digito,numero):
	if digito == 0:
		GPIO.output(PIN_DIG1, True)
		GPIO.output(PIN_DIG2, False)
	elif digito == 1:
		GPIO.output(PIN_DIG1, False)
		GPIO.output(PIN_DIG2, True)

        if numero == 0:
		GPIO.output(PIN_A, True) # segmento a
        	GPIO.output(PIN_B, True) # segmento b
        	GPIO.output(PIN_C, True) # segmento c
        	GPIO.output(PIN_D, True) # segmento d
        	GPIO.output(PIN_E, True) # segmento e
        	GPIO.output(PIN_F, True) # segmento f
	elif numero == 1:
	        GPIO.output(PIN_B, True) # segmento b
        	GPIO.output(PIN_C, True) # segmento c
	elif numero == 2:
        	GPIO.output(PIN_A, True) # segmento a
        	GPIO.output(PIN_B, True) # segmento b
        	GPIO.output(PIN_D, True) # segmento d
        	GPIO.output(PIN_E, True) # segmento e
        	GPIO.output(PIN_G, True) # segmento g
	elif numero == 3:
		GPIO.output(PIN_A, True) # segmento a
        	GPIO.output(PIN_B, True) # segmento b
        	GPIO.output(PIN_C, True) # segmento c
        	GPIO.output(PIN_D, True) # segmento d
        	GPIO.output(PIN_G, True) # segmento g
	elif numero == 4:
        	GPIO.output(PIN_B, True) # segmento b
        	GPIO.output(PIN_C, True) # segmento c
        	GPIO.output(PIN_F, True) # segmento f
        	GPIO.output(PIN_G, True) # segmento g
	elif numero == 5:
	        GPIO.output(PIN_A, True) # segmento a
        	GPIO.output(PIN_C, True) # segmento c
        	GPIO.output(PIN_D, True) # segmento d
        	GPIO.output(PIN_F, True) # segmento f
        	GPIO.output(PIN_G, True) # segmento g
	elif numero == 6:
        	GPIO.output(PIN_A, True) # segmento a
        	GPIO.output(PIN_C, True) # segmento c
        	GPIO.output(PIN_D, True) # segmento d
        	GPIO.output(PIN_E, True) # segmento e
        	GPIO.output(PIN_F, True) # segmento f
        	GPIO.output(PIN_G, True) # segmento g
	elif numero == 7:
		GPIO.output(PIN_A, True) # segmento a
        	GPIO.output(PIN_B, True) # segmento b
        	GPIO.output(PIN_C, True) # segmento c
	elif numero == 8:
		GPIO.output(PIN_A, True) # segmento a
        	GPIO.output(PIN_B, True) # segmento b
        	GPIO.output(PIN_C, True) # segmento c
        	GPIO.output(PIN_D, True) # segmento d
        	GPIO.output(PIN_E, True) # segmento e
        	GPIO.output(PIN_F, True) # segmento f
        	GPIO.output(PIN_G, True) # segmento g
	else:
		GPIO.output(PIN_A, True) # segmento a
        	GPIO.output(PIN_B, True) # segmento b
        	GPIO.output(PIN_C, True) # segmento c
        	GPIO.output(PIN_D, True) # segmento d
        	GPIO.output(PIN_F, True) # segmento f
        	GPIO.output(PIN_G, True) # segmento g


    INICIALIZAR_DISPLAY()

    GPIO.output(PIN_DIG1, False)
    GPIO.output(PIN_DIG2, False)

    while contador < 100:
	if contador < 10:
		INICIALIZAR_DISPLAY()
		PRINT_DISPLAY(0, contador)
		time.sleep(1)
	else:
		unidades = contador%10
		decimas = contador/10
		for i in range(1000):
			INICIALIZAR_DISPLAY()
			PRINT_DISPLAY(1, decimas)
			time.sleep(0.0004)
			INICIALIZAR_DISPLAY()
			PRINT_DISPLAY(0, unidades)
			time.sleep(0.0004)
	contador = contador + 1
finally: GPIO.cleanup()
