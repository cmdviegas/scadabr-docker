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
# ModbusTCP server

from pyModbusTCP.server import ModbusServer

# Create ModbusTCP server socket
server = ModbusServer("", 502, no_block=True)

try:
    server.start()
    print("Server started!")
    while True:
       continue
except:
    server.stop()
    print("Server stopped!")
