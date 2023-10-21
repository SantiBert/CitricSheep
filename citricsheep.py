import hashlib

# Paso 1: Inicializa la cadena
input_string = "CitricSheep"

# Paso 2: Calcula los valores ASCII y guárdalos en una lista
ascii_values = [ord(char) for char in input_string]

# Paso 3: Multiplica cada valor por la longitud de la cadena
multiplied_values = [value * len(input_string) for value in ascii_values]

# Paso 4: Encuentra la suma de los valores multiplicados
sum_of_values = sum(multiplied_values)

# Paso 5: Genera un hash SHA256
hash_object = hashlib.sha256(str(sum_of_values).encode())

# Paso 6: Convierte el hash a una cadena hexadecimal
hexadecimal_hash = hash_object.hexdigest()

print("Resultado final:", hexadecimal_hash)
