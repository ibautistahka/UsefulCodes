#===================================================================================================
#==   Elaborado por Ismael Bautista                                                               ==
#==   Se requiere instalar com0com para generar puertos virtuales                                 == 
#==   Se deben modificar las variables com_port1 y com_port2 segun sea la necesidad de monitoreo  ==
#===================================================================================================

#==========================================================================================
#
#           FUNCIONAMIENTO DEL PROGRAMA:
#
#
# DISPOSITIVO      FISICO          APP           VIRTUAL <--com0com-->  VIRTUAL (LIBRE)
#  _________      _________      __________      _________             _________
# |         |    |         |    |          |    |         |           |         |
# | DEVICE  |--->|com_port1|--->|sniffer.py|--->|com_port2|---------->|com_port3|
# |_________|    |_________|    |__________|    |_________|           |_________|
#
#==========================================================================================

import serial 		# pip install pyserial

baud_rate = 9600  # BAUDRATE
com_port1 = 'COM5'  # Conexión 1
com_port2 = 'COM7'  # Conexión 2

ComRead_timeout = 0.1   # Timeout cuando no hay data en el buffer
ComWr_timeout = 0.1     # Timeout cuando hay error en el buffer

log = open('log.txt', 'a+')     # Archivo log.txt para escribir data monitoreada.

From_PC_To_Device = True    # Variable que indica desde que puerto se enviara (Default= Se envio desde PC)

listener = serial.Serial(port=com_port1, baudrate=baud_rate, timeout=ComRead_timeout,
                         write_timeout=ComWr_timeout)

forwarder = serial.Serial(port=com_port2, baudrate=baud_rate, timeout=ComRead_timeout,
                          write_timeout=ComWr_timeout)


def split_hex(value):
    value = value[0:]
    return " ".join(value[i:i+2] for i in range(0, len(value), 2))
print("Conexion " + com_port1 + " (Fisico) " + " A " + com_port2 + " (Virtual)")
while 1:
	
    while (listener.inWaiting()) and From_PC_To_Device:         # inWaiting() esta en pyserial e indica espera de recepcion
        serial_out = listener.readline()                        # Transforma lo recibido en una variable
        
        Msg = "<--RX: " + " " + split_hex(serial_out.hex()).upper() + " " + " " + " " + serial_out.decode('UTF-8')
        Msg += "\n"
        log.write(Msg)     # Escribir en archivo
        print(serial_out)  # Ver desde el terminal
        forwarder.write(serial_out)                             # Se envia lo recibido al puerto 2
    else:
        From_PC_To_Device = False                               # Se envio desde dispositivo

    while (forwarder.inWaiting()) and not From_PC_To_Device:
        serial_out = forwarder.readline()                       # Transforma lo recibido en una variable
       
        Msg = "-->TX: "  + " " + split_hex(serial_out.hex()).upper() + "\n"
        log.write(Msg)     # Escribir en archivo
        print(serial_out)  # Ver desde el terminal
        listener.write(serial_out)                              # Se envia lo recibido al puerto 1
    else:
        From_PC_To_Device = True                                # Se envio desde PC
