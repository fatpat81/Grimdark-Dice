import random
import sys

def colored(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

def print_dice(rolls, threshold):
    results = []
    successes = 0
    for roll in rolls:
        if roll >= threshold:
            results.append(colored(0, 255, 136, f"[{roll}]")) # Ghost Green
            successes += 1
        else:
            results.append(colored(255, 51, 51, f"[{roll}]")) # Fail Red
    print("Dice Rolls: " + " ".join(results))
    return successes

def main():
    print(colored(74, 0, 114, "=== WARHAMMER 40K COMBAT SIMULATOR ==="))
    print(colored(0, 255, 136, "--- WARP GHOST EDITION ---\n"))
    try:
        attacks_input = input("Number of Attacks (e.g. 12): ")
        attacks = int(attacks_input)
        bs_input = input("Ballistic Skill (BS+) (2-6): ")
        bs = int(bs_input)
        if bs < 2 or bs > 6:
            print(colored(255, 51, 51, "Error: BS+ must be between 2 and 6."))
            return

        str_input = input("Strength of Attack (STR): ")
        strength = int(str_input)
    except ValueError:
        print(colored(255, 51, 51, "Invalid input. Please enter integers."))
        return

    # Step 2: Hit Roll Simulation
    print("\n" + colored(0, 255, 136, "--- HIT PHASE ---"))
    hit_rolls = [random.randint(1, 6) for _ in range(attacks)]
    hits = print_dice(hit_rolls, bs)
    print(colored(0, 255, 136, f"Total Hits: {hits}"))

    if hits == 0:
        print("No hits generated. Combat ends.")
        return

    # Step 3: Proceed or Abort
    print("\nSuccessfully Hit!")
    proceed = input("Type 'y' to 'Wound' these targets, or 'n' to stop. [y/n]: ").strip().lower()
    if proceed != 'y':
        print("Combat stopped.")
        return

    # Step 4: Wound Roll Simulation
    try:
        t_input = input("\nTarget Toughness (T): ")
        toughness = int(t_input)
    except ValueError:
        print(colored(255, 51, 51, "Invalid input for Toughness."))
        return

    # Step 5: Wound Calculation
    if strength >= 2 * toughness:
        wound_target = 2
    elif strength > toughness:
        wound_target = 3
    elif strength == toughness:
        wound_target = 4
    elif strength <= toughness / 2.0:
        wound_target = 6
    else:
        wound_target = 5  # STR < T but not half or less

    print(colored(0, 255, 136, f"Wound Target is {wound_target}+"))

    # Step 6: Final Allocation
    print("\n" + colored(0, 255, 136, "--- WOUND PHASE ---"))
    wound_rolls = [random.randint(1, 6) for _ in range(hits)]
    
    wound_results = []
    wounds_allocated = 0
    for roll in wound_rolls:
        if roll >= wound_target:
            wound_results.append(colored(0, 255, 136, f"[{roll}]")) # Ghost Green
            wounds_allocated += 1
        else:
            wound_results.append(colored(255, 51, 51, f"[{roll}]")) # Fail Red
            
    print("Wound Rolls: " + " ".join(wound_results))
    print(colored(0, 255, 255, f"\n>> {wounds_allocated} WOUNDS ALLOCATED! <<"))
    
if __name__ == "__main__":
    main()
