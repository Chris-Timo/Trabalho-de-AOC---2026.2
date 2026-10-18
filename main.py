"""
MAIN — CPU Simulada de 8 Bits
AOC 2026.2

Executa o programa autoral e apresenta a evolução
do processador durante cada ciclo de instrução.
"""

from cpu import CPU
from programas import PROGRAMA_AUTORAL


def carregar_programa(cpu, programa):
    for endereco, instrucao in enumerate(programa):
        cpu.memoria[endereco] = instrucao


def main():
    cpu = CPU()

    carregar_programa(cpu, PROGRAMA_AUTORAL)

    print("=" * 45)
    print("       CPU SIMULADA — 8 BITS")
    print("=" * 45)
    print("PROGRAMA AUTORAL")
    print(f"Quantidade de instruções: {len(PROGRAMA_AUTORAL)}")
    print("=" * 45)

    cpu.executar()

    print("\n" + "=" * 45)
    print("             RESULTADO FINAL")
    print("=" * 45)

    cpu.mostrar_estado()

    print("\nMemória utilizada pelo programa:")
    print(f"Memória[14]: {cpu.memoria[14]}")
    print(f"Memória[15]: {cpu.memoria[15]}")

    print("=" * 45)


if __name__ == "__main__":
    main()