import random
import time
import math

# -------- Level Settings --------
def get_level_settings(level_num):
    if level_num == 1:
        return 1, 10, 3, 'all'
    elif level_num == 2:
        return 11, 99, 4, 'all'
    elif level_num == 3:
        return 100, 999, 6, 'all'
    elif level_num == 4:
        return 2, 100, 5, 'even'
    elif level_num == 5:
        return 3, 60, 4, 'multiple3'
    elif level_num == 6:
        return 4, 80, 4, 'multiple4'
    elif level_num == 7:
        return 5, 100, 4, 'multiple5'
    elif level_num == 8:
        return 6, 120, 4, 'multiple6'
    elif level_num == 9:
        return 7, 140, 4, 'multiple7'
    elif level_num == 10:
        return 8, 160, 4, 'multiple8'
    elif level_num == 11:
        return 9, 180, 4, 'multiple9'
    elif level_num == 12:
        return 10, 200, 4, 'multiple10'
    elif level_num == 13:
        return 2, 100, 5, 'prime'
    elif level_num == 14:
        return 1, 200, 5, 'squareroot'
    elif level_num == 15:
        return 1, 200, 5, 'cuberoot'
    return None, None, None, None

# -------- Player Input --------
def get_player_guess(player, low, high, filter_type):
    while True:
        try:
            guess = int(input(f"\U0001F464 Player {player}, enter your guess ({low}-{high}): "))
            if low <= guess <= high:
                if filter_type == 'even' and guess % 2 != 0:
                    print("⚠️ Only even numbers are allowed at this level!")
                elif filter_type.startswith('multiple') and guess % int(filter_type.replace('multiple', '')) != 0:
                    print(f"⚠️ Only multiples of {filter_type.replace('multiple', '')} are allowed at this level!")
                elif filter_type == 'prime' and not is_prime(guess):
                    print("⚠️ Only prime numbers are allowed at this level!")
                elif filter_type == 'squareroot' and not is_perfect_square(guess):
                    print("⚠️ Only perfect squares are allowed at this level!")
                elif filter_type == 'cuberoot' and not is_perfect_cube(guess):
                    print("⚠️ Only perfect cubes are allowed at this level!")
                else:
                    return guess
            else:
                print(f"⚠️ Number must be between {low} and {high}.")
        except ValueError:
            print("⚠️ Please enter a valid number.")

# -------- Prime/Square/Cube Checks --------
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect_square(n):
    return int(math.isqrt(n)) ** 2 == n

def is_perfect_cube(n):
    return round(n ** (1/3)) ** 3 == n

# -------- Game Mode Selection --------
def choose_mode():
    print("\U0001f3ae Choose Game Mode:")
    print("1. Single Player (You vs Computer)")
    print("2. Two Player (Player A vs Player B)")
    while True:
        mode = input("Enter 1 or 2: ")
        if mode in ['1', '2']:
            return int(mode)
        print("⚠️ Invalid choice. Try again.")

# -------- Core Gameplay --------
def play_game():
    mode = choose_mode()
    is_single_player = (mode == 1)
    player_scores = {'A': 0, 'B': 0}
    current_level = 1
    highest_level_reached = 0
    lifeline_used = False

    while True:
        settings = get_level_settings(current_level)
        if not settings:
            break
        low, high, max_attempts, filter_type = settings
        valid_numbers = [n for n in range(low, high + 1) if
                         (filter_type == 'even' and n % 2 == 0) or
                         (filter_type.startswith('multiple') and n % int(filter_type.replace('multiple', '')) == 0) or
                         (filter_type == 'prime' and is_prime(n)) or
                         (filter_type == 'squareroot' and is_perfect_square(n)) or
                         (filter_type == 'cuberoot' and is_perfect_cube(n)) or
                         filter_type == 'all']
        secret_number = random.choice(valid_numbers)
        min_bound, max_bound = low, high
        computer_guesses = set()
        retry_used = False

        print(f"\n🤙 LEVEL {current_level}: Guess the number between {low} and {high}")
        if filter_type != 'all':
            print(f"⚠️ Note: Only {filter_type.upper()} numbers are valid at this level!")
        print(f"🎯 {max_attempts} attempts per player this level.")

        winner = None

        for attempt in range(1, max_attempts + 1):
            print(f"\n🔁 Round {attempt} of {max_attempts}")

            guess_a = get_player_guess('A', low, high, filter_type)
            if guess_a == secret_number:
                winner = 'A'
                break
            else:
                print("❌ Wrong guess, Player A.")
                print(f"📉 You were off by {abs(secret_number - guess_a)}.")
                if guess_a < secret_number:
                    print("⬆️ Hint: Try a * HIGHER * number.")
                    min_bound = max(min_bound, guess_a + 1)
                else:
                    print("⬇️ Hint: Try a * LOWER * number.")
                    max_bound = min(max_bound, guess_a - 1)

            if is_single_player:
                print("🤖 Computer is thinking...")
                time.sleep(1)
                guess_b = None

                range_pool = [x for x in range(min_bound, max_bound + 1) if x not in computer_guesses and
                              ((filter_type == 'even' and x % 2 == 0) or
                               (filter_type.startswith('multiple') and x % int(filter_type.replace('multiple', '')) == 0) or
                               (filter_type == 'prime' and is_prime(x)) or
                               (filter_type == 'squareroot' and is_perfect_square(x)) or
                               (filter_type == 'cuberoot' and is_perfect_cube(x)) or
                               filter_type == 'all')]

                mid = (min_bound + max_bound) // 2
                guess_b = min(range_pool, key=lambda x: abs(x - mid)) if range_pool else random.choice(valid_numbers)

                computer_guesses.add(guess_b)
                print(f"🤖 Computer guesses: {guess_b}")

                if guess_b == secret_number:
                    winner = 'B'
                    break
                else:
                    print("🤖 Computer guessed wrong.")
                    if guess_b < secret_number:
                        print(f"💡 Computer whispers: Try **higher than {guess_b}** next time...")
                        min_bound = max(min_bound, guess_b + 1)
                    else:
                        print(f"💡 Computer suggests: Try **lower than {guess_b}** next round...")
                        max_bound = min(max_bound, guess_b - 1)
            else:
                guess_b = get_player_guess('B', low, high, filter_type)
                if guess_b == secret_number:
                    winner = 'B'
                    break
                else:
                    print("❌ Wrong guess, Player B.")
                    print(f"📉 Off by {abs(secret_number - guess_b)}")
                    if guess_b < secret_number:
                        print("⬆️ Hint: Try a **higher** number.")
                    else:
                        print("⬇️ Hint: Try a **lower** number.")

        if winner:
            label = "You" if is_single_player and winner == 'A' else "Computer" if is_single_player else f"Player {winner}"
            print(f"\n🏆 {label} guessed correctly!")
            player_scores[winner] += 1
            highest_level_reached = max(highest_level_reached, current_level)
            current_level += 1
            time.sleep(1)
        else:
            if not retry_used:
                print("\n🛑 No one guessed correctly. Granting a one-time retry for this level!")
                retry_used = True
                secret_number = random.choice(valid_numbers)  # regenerate
                continue  # retry this level
            else:
                print("\n🛑 Game Over. You've used your retry.")
                print(f"🔐 The secret number was: {secret_number}")
                break

    print("\n📊 Final Scores:")
    print(f"Player A: {player_scores['A']}")
    print(f"Player B: {player_scores['B']}")
    print(f"🔝 Highest Level Reached: {highest_level_reached}")
    if player_scores['A'] > player_scores['B']:
        print("🎉 You win!" if is_single_player else "🎉 Player A wins!")
    elif player_scores['B'] > player_scores['A']:
        print("💻 Computer wins!" if is_single_player else "🎉 Player B wins!")
    else:
        print("🤝 It's a tie!")
    time.sleep(1)

# -------- Game Loop --------
def level_up_game():
    print("\U0001f3ae Welcome to the Number Guessing Game!")
    while True:
        play_game()
        again = input("\n🔁 Play again? (y/n): ").strip().lower()
        if again != 'y':
            print("👋 Goodbye!")
            break
        print("\n🔁 Restarting...\n")
        time.sleep(1)

# -------- Run Game --------
if __name__ == "__main__":
    level_up_game()
