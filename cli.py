import computer , cpu, memory

import sys

print("======================================================================")
print( "Sistema Operacional:",computer.distro(),computer.osVersion())
print("Tipo de Processador:",computer.cpu())
print("Arquitetura:",computer.arc())
print("Velocidade:", cpu.freq(),"GHz")
print("Nucleos:", cpu.cores())
print("Nucleos Fisicos:",cpu.phycores())
print("Memoria:",memory.size(),"Gb")
print("Nome Do Computador:",computer.name())
print("======================================================================")