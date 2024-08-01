# ██████╗  ██████╗ █████╗
# ██╔══██╗██╔════╝██╔══██╗
# ██║  ██║██║     ███████║
# ██║  ██║██║     ██╔══██║
# ██████╔╝╚██████╗██║  ██║
# ╚═════╝  ╚═════╝╚═╝  ╚═╝
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE, NATAL/RN
#
# (C) 2024 CARLOS M D VIEGAS
# https://github.com/cmdviegas

### Description:
# This script simulates the filling of a tank during which
# an LED lights up indicating the filling and turns off when
# emptying. It uses ModbusTCP as communcation protocol.

from pyModbusTCP.client import ModbusClient
import time

# Create ModbusClient socket
client = ModbusClient(host="127.0.0.1", port=502, auto_open=True)

# Start LED and TANK LEVEL with 0
led_status = 0 # 0-1
led_datapoint = client.write_single_register(1, led_status) # (id, value)

tank_level = 0 # 0-100
tank_datapoint = client.write_single_register(2, tank_level)

while True:
    # Connect modbus client to server
    client.open()

    if (tank_level == 0):
        print ("Tank is empty!")
        time.sleep(1)

    # Filling tank
    print ("Start filling tank...")
    while tank_level < 100:
        led_status = 1
        print("LED is on - tank level = ", tank_level)

        client.write_single_register(1, led_status) # Turn on LED

        tank_level = tank_level + 10

        client.write_single_register(2, tank_level) # Increase TANK LEVEL by 10

        time.sleep(2)

    if (tank_level == 100):
        print ("Tank is full!")
        time.sleep(5)
    else:
        break

    # Draining tank
    print ("Draining tank...")
    while tank_level > 0:
        led_status = 0
        print("LED is off - tank level = ", tank_level)

        client.write_single_register(1, led_status) # Turn off LED

        tank_level = tank_level - 10

        client.write_single_register(2, tank_level) # Decrease TANK LEVEL by 10

        time.sleep(2)
