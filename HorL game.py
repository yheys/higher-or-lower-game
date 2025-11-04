import random

vs = """
__       __       _____ 
\ \     / /      / ____|
 \ \  /  /      | (___  
  \ \/  /        \___ \ 
   \   /         ____) |
    \_/         |_____/  

"""

football_players = [
    {"name": "Kylian Mbappé", "rating": 92},
    {"name": "Erling Haaland", "rating": 91},
    {"name": "Kevin De Bruyne", "rating": 91},
    {"name": "Lionel Messi", "rating": 90},
    {"name": "Jude Bellingham", "rating": 90},
    {"name": "Vinícius Jr.", "rating": 90},
    {"name": "Mohamed Salah", "rating": 89},
    {"name": "Rodri", "rating": 89},
    {"name": "Harry Kane", "rating": 89},
    {"name": "Neymar Jr.", "rating": 88},
    {"name": "Bruno Fernandes", "rating": 88},
    {"name": "Luka Modrić", "rating": 87},
    {"name": "Robert Lewandowski", "rating": 87},
    {"name": "Bukayo Saka", "rating": 86},
    {"name": "Son Heung-min", "rating": 86},
    {"name": "Ousmane Dembélé", "rating": 85},
    {"name": "Federico Valverde", "rating": 85},
    {"name": "Lautaro Martínez", "rating": 85},
    {"name": "Bernardo Silva", "rating": 84},
    {"name": "Pedri", "rating": 84}
]
print("welcome to yheys higher or lower game based on top players 2025 rating")
score = 0
you_get_the_ansewer = True
B = random.choice(football_players)
while you_get_the_ansewer:
    A = B
    B = random.choice(football_players)
    if A==B:
        B=random.choice(football_players)
    for_guess = {"A": A, "B": B, }
    print(f" Compare A: {A["name"]} \n {vs}\n  Aganest B: {B["name"]}")
    rate_A = A["rating"]
    rate_B = B["rating"]
    guess = input("which player has higher rate in 2025?  write 'A' or 'B': ").upper()
    print(f"{A["name"]} has {A["rating"]} rate.\n{B["name"]} has {B["rating"]} rate. ")
    your_guess = for_guess[guess]
    if rate_A > rate_B:
        higher = rate_A
    elif rate_A == rate_B:
        higher = rate_B
        print("both are equal")
    else:
        higher = rate_B
    score += 1
    print(f"your score is {score}")
    if your_guess["rating"] != higher:
        you_get_the_ansewer = False
        print(f"you fail and the score is {score}")