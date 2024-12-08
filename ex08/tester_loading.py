from tqdm import tqdm
import time

# from Loading import ft_tqdm
# for elem in ft_tqdm(range(333)):
    # sleep(0.005)
# print()
for elem in tqdm(range(333)):
    time.sleep(0.005)
print(tqdm.__doc__)

# Lista de cadenas de ejemplo
strings = ['Hola', 'Mundo', 'en', 'Python']

# Iteración sobre la lista con tqdm
for string in tqdm(strings, desc='Procesando cadenas'):
    # Simulamos una operación que toma tiempo
    time.sleep(0.5)
    print(string)

