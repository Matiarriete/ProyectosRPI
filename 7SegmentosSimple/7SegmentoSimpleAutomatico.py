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
    def INICIALIZAR_DISPLAY():
        # si enviamos 0 apagamos los segmentos
        time.sleep(1)
	GPIO.output(PIN_A, False)
        GPIO.output(PIN_B, False)
        GPIO.output(PIN_C, False)
        GPIO.output(PIN_D, False)
        GPIO.output(PIN_E, False)
        GPIO.output(PIN_F, False)
        GPIO.output(PIN_G, False)
        GPIO.output(PIN_DP, False)
    def PRINT_DISPLAY():

        GPIO.output(PIN_A, True) # segmento a
        GPIO.output(PIN_B, True) # segmento b
        GPIO.output(PIN_C, True) # segmento c
        GPIO.output(PIN_D, True) # segmento d
        GPIO.output(PIN_E, True) # segmento e
        GPIO.output(PIN_F, True) # segmento f

	INICIALIZAR_DISPLAY()

        GPIO.output(PIN_B, True) # segmento b
        GPIO.output(PIN_C, True) # segmento c

	INICIALIZAR_DISPLAY()

        GPIO.output(PIN_A, True) # segmento a
        GPIO.output(PIN_B, True) # segmento b
        GPIO.output(PIN_D, True) # segmento d
        GPIO.output(PIN_E, True) # segmento e
        GPIO.output(PIN_G, True) # segmento g

	INICIALIZAR_DISPLAY()

        GPIO.output(PIN_A, True) # segmento a
        GPIO.output(PIN_B, True) # segmento b
        GPIO.output(PIN_C, True) # segmento c
        GPIO.output(PIN_D, True) # segmento d
        GPIO.output(PIN_G, True) # segmento g

	INICIALIZAR_DISPLAY()

        GPIO.output(PIN_B, True) # segmento b
        GPIO.output(PIN_C, True) # segmento c
        GPIO.output(PIN_F, True) # segmento f
        GPIO.output(PIN_G, True) # segmento g

	INICIALIZAR_DISPLAY()

        GPIO.output(PIN_A, True) # segmento a
        GPIO.output(PIN_C, True) # segmento c
        GPIO.output(PIN_D, True) # segmento d
        GPIO.output(PIN_F, True) # segmento f
        GPIO.output(PIN_G, True) # segmento g

        INICIALIZAR_DISPLAY()

        GPIO.output(PIN_A, True) # segmento a
        GPIO.output(PIN_C, True) # segmento c
        GPIO.output(PIN_D, True) # segmento d
        GPIO.output(PIN_E, True) # segmento e
        GPIO.output(PIN_F, True) # segmento f
        GPIO.output(PIN_G, True) # segmento g

        INICIALIZAR_DISPLAY()

        GPIO.output(PIN_A, True) # segmento a
        GPIO.output(PIN_B, True) # segmento b
        GPIO.output(PIN_C, True) # segmento c

        INICIALIZAR_DISPLAY()

        GPIO.output(PIN_A, True) # segmento a
        GPIO.output(PIN_B, True) # segmento b
        GPIO.output(PIN_C, True) # segmento c
        GPIO.output(PIN_D, True) # segmento d
        GPIO.output(PIN_E, True) # segmento e
        GPIO.output(PIN_F, True) # segmento f
        GPIO.output(PIN_G, True) # segmento g

        INICIALIZAR_DISPLAY()

        GPIO.output(PIN_A, True) # segmento a
        GPIO.output(PIN_B, True) # segmento b
        GPIO.output(PIN_C, True) # segmento c
        GPIO.output(PIN_D, True) # segmento d
        GPIO.output(PIN_F, True) # segmento f
        GPIO.output(PIN_G, True) # segmento g

	time.sleep(1)

    INICIALIZAR_DISPLAY()

    time.sleep(0.5)

    PRINT_DISPLAY()

finally: GPIO.cleanup()
