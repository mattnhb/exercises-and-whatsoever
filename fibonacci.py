from typing import List


def get_fibonacci_list(numero) -> List[int]:
    minha_lista = [0, 1]
    for _ in range(numero - 2):
        minha_lista.append(minha_lista[-1] + minha_lista[-2])
    return minha_lista


numero: int = int(input("Quantos elementos a lista deve ter? "))

lista_fibonacci = get_fibonacci_list(numero)
print(lista_fibonacci)
