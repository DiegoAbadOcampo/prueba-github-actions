import os

archivo = "contador.txt"

# Leer valor actual
if os.path.exists(archivo):
    with open(archivo, "r") as f:
        contador = int(f.read().strip())
else:
    contador = 0

# Sumar 1
contador += 1

# Guardar nuevo valor
with open(archivo, "w") as f:
    f.write(str(contador))

print(f"Contador actualizado: {contador}")