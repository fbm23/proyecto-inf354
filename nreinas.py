import pandas as pd
import numpy as np
import random

def initialize_board(n):
    return list(range(n))

def calculate_attacks(board):
    attacks = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                attacks += 1
    return attacks

def simulated_annealing(n, temperature=10000, cooling_rate=0.995):
    current_board = initialize_board(n)
    random.shuffle(current_board)
    current_attacks = calculate_attacks(current_board)
    best_board = current_board[:]
    best_attacks = current_attacks
    
    while temperature > 0.1 and best_attacks != 0:
        new_board = current_board[:]
        i, j = random.sample(range(n), 2)
        new_board[i], new_board[j] = new_board[j], new_board[i]
        new_attacks = calculate_attacks(new_board)
        
        if new_attacks < current_attacks:
            current_board = new_board[:]
            current_attacks = new_attacks
            if current_attacks < best_attacks:
                best_board = current_board[:]
                best_attacks = current_attacks
        else:
            if random.random() < np.exp((current_attacks - new_attacks) / temperature):
                current_board = new_board[:]
                current_attacks = new_attacks
        
        temperature *= cooling_rate
        
    return best_board, best_attacks

# Generar combinaciones simuladas
n = 8  # Número de reinas
solutions = []

for _ in range(5):  # Generar 5 soluciones simuladas
    board, attacks = simulated_annealing(n)
    solutions.append((board, attacks))

# Guardar las soluciones en un archivo Excel
df = pd.DataFrame(solutions, columns=['Board Configuration', 'Attacks'])
df.to_excel('n_queens_solutions.xlsx', index=False)
