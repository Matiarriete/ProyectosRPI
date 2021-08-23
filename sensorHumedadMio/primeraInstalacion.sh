#https://descubrearduino.com/temperatura-humedad-raspberry-pi/
#!/bin/bash

codigoRepetitivo(){
#	clear
	for numero in {1,2};
	do
        	echo "--------------------"
	done
	echo  $1
	for numero in {1,2};
        do
                echo "--------------------"
        done
}
codigoRepetitivo "Haciendo update"
sudo apt-get update

codigoRepetitivo "Haciendo upgrade"
sudo apt-get upgrade -y

codigoRepetitivo "Instalando dependencias"
sudo apt-get install build-essential python-dev python-openssl git

codigoRepetitivo "Instalando programa"
cd Adafruit_Python_DHT
sudo python setup.py install
cd ..
sudo chmod 777 ejecutarHumedad.sh

codigoRepetitivo "Instalado sin fallos"

