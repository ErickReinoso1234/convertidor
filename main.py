#Convertidor a decimal a binario
print("De decimal a binario")
numero = int(input("Introduce un número decimal: "))
binario = bin(numero)[2:]
print(f"El número {numero} en binario es: {binario}")

#Convertidor de binario a decimal
print("De binario a decimal")
entero = input("Introduce un número en binario: ")
enteros = int(entero, 2)
print(f"El número binario {entero} en decimal es: {enteros}")

#Decimal a octeto
print("Decimal a octeto")
octeto = int(input("Introduce un número en decimal: "))
octetos = oct(octeto)[2:]
print(f"El número decimal {octeto} el octeto es: {octetos}")

#Octeto a decimal
print("Octeto a decimal")
octal = input("Introduce un número en octal: ")
decimal = int(octal, 8)
print(f"El número octal {octal} en decimal es: {decimal}")

# Hexadecimal a octal
print("Hexadecimal a octal")
hexadecimal = input("Introduce un número en hexadecimal: ")
decimal = int(hexadecimal, 16)
octal = oct(decimal)[2:] 
print(f"El número hexadecimal {hexadecimal} en octal es: {octal}")

# octal a hexadecimal
print("Octal a hexadecimal")
octal = input("Introduce un número en octal: ")
decimal = int(octal, 8)
hexadecimal = hex(decimal)[2:].upper() 
print(f"El número octal {octal} en hexadecimal es: {hexadecimal}")

# Binario a octal
print("Binario a octal")
binario = input("Introduce un número en binario: ")
decimal = int(binario, 2)
octal = oct(decimal)[2:] 
print(f"El número binario {binario} en octal es: {octal}")

# De octeto a binario
print("Octal a binario")
octal = input("Introduce un número en octal: ")
decimal = int(octal, 8)
binario = bin(decimal)[2:] 
print(f"El número octal {octal} en binario es: {binario}")

# De octal a decimal
print("Octal a decimal")
octal = input("Introduce un número en octal: ")
decimal = int(octal, 8)
print(f"El número octal {octal} en decimal es: {decimal}")

# De decimal a octal
print("decimal a octal")
decimal = int(input("Introduce un número decimal: "))
octal = oct(decimal)[2:] 
print(f"El número decimal {decimal} en octal es: {octal}")
