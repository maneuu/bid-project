import os
from art import logo 

# Função para limpar o terminal, dependendo do sistema operacional
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear') 

# Dicionário para armazenar os lances
bid_dictionary = {}

active = True
print(logo)

# Loop principal que coleta os lances dos usuários
while active:
    name = input("Hello! What's your name? ")
    # Evita que o nome esteja em branco
    if name == "":
        print("Type a valid name")
        continue

    # Verificação para garantir que o lance inserido seja um número válido
    while True:
        try:
            bid = int(input("Please enter your bid amount in dollars: $ "))
            break  # Sai do loop se a entrada for válida
        except ValueError:
            print("Oops! Please enter a valid number for the bid.")

    # Verifica se o nome já foi utilizado e solicita novamente se necessário
    if name in bid_dictionary:
        print(f"{name}, you have already placed a bid. Please enter a different name.")
        continue  # Retorna ao começo do loop

    # Adiciona o nome e o valor do lance ao dicionário
    bid_dictionary[name] = bid

    # Loop para garantir que a resposta seja 'yes' ou 'no'
    while True:
        repeat = input("Are there any other bidders? Type 'yes' if someone else wants to bid, or 'no' if you're done. \n\t").lower()
        if repeat in ['yes', 'no']:
            break
        else:
            print("Invalid input! Please type 'yes' or 'no'.")

    # Se não houver mais lances, termina o loop
    if repeat == "no":
        active = False
    
    # Limpa o terminal 
    clear_terminal()

# Variáveis para determinar o vencedor
highest_bid = 0  
winner = "" 

# Loop para percorrer todos os lances e encontrar o maior
for user in bid_dictionary:
    value = bid_dictionary[user]
    
    if value > highest_bid:
        winner = user
        highest_bid = value

print(f"🎉 Congratulations, {winner}! You are the winner with an amazing bid of ${highest_bid}! 🎉")