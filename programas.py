# ==============================================
# PROGRAMA AUTORAL
# ==============================================
# Processa dois valores usando operações aritméticas
# e lógicas, armazenando resultados na memória.
#
# A = 12
# B = 10
# Soma = A + B = 22
# XOR = A XOR B = 6
# Resultado final = Soma - XOR = 16

PROGRAMA_AUTORAL = [
    "LOAD R0, 12",
    "LOAD R1, 10",
    "ADD R0, R1",
   "STORE R0, 14",
    "LOAD R2, 12",
    "XOR R1, R2",
    "SUB R0, R1",
    "STORE R0, 15",
    "HALT"
]