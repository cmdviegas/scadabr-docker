from pyModbusTCP.client import ModbusClient
import time

client = ModbusClient(host="127.0.0.1", port=502, auto_open=True)

led = client.write_single_register(1,0)

while True:

    client.open()

    led = client.read_holding_registers(1)
     
    # liga led
    print("led on")
    client.write_single_register(1,1)
    time.sleep(5)

    # desliga led
    print("led off")
    client.write_single_register(1,0)
    time.sleep(5)
