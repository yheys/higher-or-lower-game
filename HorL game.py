import random

vs = """
 __        __       _____ 
 \\ \\     / /      / ___|
  \\ \\  /  /      | (___  
   \\ \\/  /        \\___\
    \\   /         ____) |
     \\_/         |_____/  
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

print("Welcome to Yheys Higher or Lower game (Top Players 2025 Ratings) ⚽")

score = 0
game_on = True

B = random.choice(football_players)

while game_on:
    A = B
    B = random.choice(football_players)

    while A == B:
        B = random.choice(football_players)

    print(f"\nCompare A: {A['name']}")
    print(vs)
    print(f"Against B: {B['name']}")

    guess = input("Which player has higher rating in 2025? Type 'A' or 'B': ").upper()

    if guess not in ["A", "B"]:
        print("Invalid input! Game over.")
        break

    print(f"\n{A['name']} has {A['rating']} rating.")
    print(f"{B['name']} has {B['rating']} rating.")

    if A["rating"] > B["rating"]:
        correct_answer = "A"
    elif B["rating"] > A["rating"]:
        correct_answer = "B"
    else:
        print("Both players have equal ratings!")
        correct_answer = guess  # both correct

    if guess == correct_answer:
        score += 1
        print(f"✅ Correct! Your score is {score}")
    else:
        print(f"❌ Wrong! Final score: {score}")
        game_on = False