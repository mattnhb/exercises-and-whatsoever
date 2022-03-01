# O objetivo do jogo é ter uma pilha (rod) com [3, 2, 1]
from typing import Tuple, List, Dict
import os


def clear() -> None:
    command = "clear" if os.name != "nt" else "cls"
    os.system(command)


def create_rods() -> Tuple[List[int]]:
    return [3, 2, 1], [], []


def create_rods_dictionary() -> Dict[str, List[int]]:
    return dict(zip(["a", "b", "c"], create_rods()))


def move_disk(origin_index, destination_index) -> None:
    origin_rod = rod_dictionary.get(origin_index)
    destination_rod = rod_dictionary.get(destination_index)
    destination_rod.append(origin_rod.pop())


def print_rods() -> None:
    print("*********Atualmente*********")
    print(f"rod_a = {rod_dictionary.get('a')}")
    print(f"rod_b = {rod_dictionary.get('b')}")
    print(f"rod_c = {rod_dictionary.get('c')}")
    print("****************************")


def game() -> None:
    while rod_dictionary.get("b") != [3, 2, 1] and rod_dictionary.get("c") != [3, 2, 1]:
        try:
            print_rods()
            origem, destino = (
                input("Digite a origem e o destino [A, B, C] no formato 'O D' ")
                .lower()
                .split()
            )
            if origem not in ["a", "b", "c"] or destino not in ["a", "b", "c"]:
                clear()
                print("As únicas letras aceitáveis para esse exercício são A, B e C")
                continue
            move_disk(origem, destino)
            clear()
        except ValueError:
            clear()
            print("Formato 'O D', por favor")
        except IndexError:
            clear()
            print("Você está tentando remover um disco de uma rod vazia")
    print("Você ganhou o jogo!")

if __name__ == "__main__":
    rod_dictionary = create_rods_dictionary()
    game()
