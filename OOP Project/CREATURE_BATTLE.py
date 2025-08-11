from abc import ABC, abstractmethod

class Creature(ABC):

    def __init__(self):
        self.__health = 100
        self.__name = ""

    def set_health(self, new_health):
        self.__health = new_health
        # Update the '<Creature>_data' dictionary if it exists in the subclass
        if hasattr(self, '__Dragon_data'):
            self.__Dragon_data['health'] = new_health
        elif hasattr(self, '__Wizard_data'):
            self.__Wizard_data['health'] = new_health
        elif hasattr(self, '__Elf_data'):
            self.__Elf_data['health'] = new_health

    def set_name(self, user_name, creature):
        self.__name = user_name
        print(f"Creature '{self.__name}' ({creature}) created successfully!")

    def get_health(self):
        return self.__health

    def get_name(self):
        return self.__name

    def reduce_health(self, opponent, amount=0.95):
        new_health = opponent.get_health() * amount
        opponent.set_health(new_health)
        return f"{opponent.get_name()}'s remaining health: {opponent.get_health()}"

    @classmethod
    def view_creatures(self, dictionary, creature):
        for name, health in dictionary.items():
            return f"-> {dictionary['name']} ({creature}) - Health: {dictionary['health']}"

    @abstractmethod
    def attack():
        pass

    @abstractmethod
    def special_move():
        pass


class Dragon(Creature):
    __Dragon_data = {}

    def __init__(self):
        super().__init__()
        print("\nInside Constructor, A dragon is created!")

    def set_name(self, user_name):
        super().set_name(user_name, self.__class__.__name__)
        self.__Dragon_data['name'] = self.get_name()
        self.__Dragon_data['health'] = self.get_health()

    def get_Dragon_data(self):
        return self.__Dragon_data

    @classmethod
    def view_creatures(cls):
        return super().view_creatures(cls.__Dragon_data, cls.__name__)

    def attack(self, opponent):
        print(f"{self.get_name()} breathed fire at {opponent.get_name()}!")
        return super().reduce_health(opponent, 0.95)

    def special_move(self, opponent):
        print(f"{self.get_name()} leaked poison gas at {opponent.get_name()}!")
        return super().reduce_health(opponent, 0.85)


class Wizard(Creature):
    __Wizard_data = {}

    def __init__(self):
        super().__init__()
        print("\nInside Constructor, A wizard is created!")

    def set_name(self, user_name):
        super().set_name(user_name, self.__class__.__name__)
        self.__Wizard_data['name'] = self.get_name()
        self.__Wizard_data['health'] = self.get_health()

    @classmethod
    def view_creatures(cls):
        return super().view_creatures(cls.__Wizard_data, cls.__name__)

    def get_Wizard_data(self):
        return self.__Wizard_data

    def attack(self, opponent):
        print(f"{self.get_name()} launched fireball at {opponent.get_name()}!")
        return super().reduce_health(opponent, 0.95)

    def special_move(self, opponent):
        print(f"{self.get_name()} fired magic beam at {opponent.get_name()}!")
        return super().reduce_health(opponent, 0.85)


class Elf(Creature):
    __Elf_data = {}

    def __init__(self):
        super().__init__()
        print("\nInside Constructor, An Elf is created!")

    def set_name(self, user_name):
        super().set_name(user_name, self.__class__.__name__)
        self.__Elf_data['name'] = self.get_name()
        self.__Elf_data['health'] = self.get_health()

    def get_Elf_data(self):
        return self.__Elf_data

    @classmethod
    def view_creatures(cls):
        return super().view_creatures(cls.__Elf_data, cls.__name__)

    def attack(self, opponent):
        print(f"{self.get_name()} launched fireball at {opponent.get_name()}!")
        return super().reduce_health(opponent, 0.95)

    def special_move(self, opponent):
        print(f"{self.get_name()} fired magic beam at {opponent.get_name()}!")
        return super().reduce_health(opponent, 0.85)

def main_menu():
    print("\n==============================")
    print("    FANTASY CREATURE BATTLE")
    print("==============================")
    print("1. Create Creature\n2. View Creatures\n3. Start Battle\n4. Exit")
    print("==============================")
    print("Choose an option: ", end="")
    while True:
        try:
            user_input = int(input())
            if 1 <= user_input <= 4:
                return user_input
            else:
                print("Please enter a number between 1 and 4: ", end="")
        except ValueError:
            print('Error: Please enter a number only: ', end="")

def create_creature():
    while True:
        print("Choose Creature Type:\n1. Dragon\n2. Wizard\n3. Elf")
        try:
            user_choice = int(input("Choose: "))
            creature_name = input("Enter creature name: ")
            
            if user_choice == 1:
                drg = Dragon()
                drg.set_name(creature_name)
                break
            elif user_choice == 2:
                wiz = Wizard()
                wiz.set_name(creature_name)
                break
            elif user_choice == 3:
                elf = Elf()
                elf.set_name(creature_name)
                break
            else:
                print("Wrong Choice!")
        except ValueError as VE:
            print(f'Error: {VE}')

def view_creatures():
    # print(Dragon.view_creatures())
    # print(Wizard.view_creatures())
    # print(Elf.view_creatures())
    dragon_data = Dragon.get_Dragon_data(Dragon())
    wizard_data = Wizard.get_Wizard_data(Wizard())
    elf_data = Elf.get_Elf_data(Elf())
    
    print("\n=== CREATURES ===")
    if dragon_data:
        print(f"{dragon_data['name']} (Dragon) - Health: {dragon_data['health']}")
    else:
        print("No Dragons created yet.")
    
    if wizard_data:
        print(f"{wizard_data['name']} (Wizard) - Health: {wizard_data['health']}")
    else:
        print("No Wizards created yet.")
    
    if elf_data:
        print(f"{elf_data['name']} (Elf) - Health: {elf_data['health']}")
    else:
        print("No Elves created yet.")
    print("================")

def start_battle():
    # Check if there are any creatures to battle with
    dragon_data = Dragon.get_Dragon_data(Dragon())
    wizard_data = Wizard.get_Wizard_data(Wizard())
    elf_data = Elf.get_Elf_data(Elf())
    
    creatures = [] # this list has three tuples (creature_type, creature_data) for each creature 
    
    # Collect all available creatures
    if dragon_data:
        creatures.append(("Dragon", dragon_data))
    if wizard_data:
        creatures.append(("Wizard", wizard_data))
    if elf_data:
        creatures.append(("Elf", elf_data))
    
    if len(creatures) < 2:
        print("\nError: You need at least 2 creatures to start a battle!")
        print("Please create more creatures first.")
        return
    
    print("\nAvailable Creatures:")
    for i, (creature_type, data) in enumerate(creatures, 1):
        print(f"{i}. {creature_type}: {data['name']} - Health: {data['health']}")
    
    try:
        # Get creature choices
        print(f"\nChoose two creatures to battle (1-{len(creatures)}):")
        attacker_choice = int(input("Choose first creature (attacker): ")) - 1
        opponent_choice = int(input("Choose second creature (opponent): ")) - 1
        
        # Validate choices
        if (attacker_choice < 0 or attacker_choice >= len(creatures) or 
            opponent_choice < 0 or opponent_choice >= len(creatures) or
            attacker_choice == opponent_choice):
            print("Invalid choice! Please select different creatures between 1 and", len(creatures))
            return
        
        # Get creature types and names
        attacker_type, attacker_data = creatures[attacker_choice]
        opponent_type, opponent_data = creatures[opponent_choice]
        
        print(f"\n{attacker_data['name']} ({attacker_type}) vs {opponent_data['name']} ({opponent_type})")
        print("=" * 50)
        
        # Create creature instances for battle
        if attacker_type == "Dragon":
            attacker = Dragon()
            attacker.set_name(attacker_data['name'])
            attacker.set_health(attacker_data['health'])
        elif attacker_type == "Wizard":
            attacker = Wizard()
            attacker.set_name(attacker_data['name'])
            attacker.set_health(attacker_data['health'])
        elif attacker_type == "Elf":
            attacker = Elf()
            attacker.set_name(attacker_data['name'])
            attacker.set_health(attacker_data['health'])
        
        if opponent_type == "Dragon":
            opponent = Dragon()
            opponent.set_name(opponent_data['name'])
            opponent.set_health(opponent_data['health'])
        elif opponent_type == "Wizard":
            opponent = Wizard()
            opponent.set_name(opponent_data['name'])
            opponent.set_health(opponent_data['health'])
        elif opponent_type == "Elf":
            opponent = Elf()
            opponent.set_name(opponent_data['name'])
            opponent.set_health(opponent_data['health'])
        
        # Battle loop
        round_num = 1
        while attacker.get_health() > 0 and opponent.get_health() > 0:
            print(f"\n--- Round {round_num} ---")
            print(f"{attacker.get_name()}: {attacker.get_health():.1f} HP")
            print(f"{opponent.get_name()}: {opponent.get_health():.1f} HP")
            
            # First creature's turn (attacker)
            print(f"\nNow {attacker.get_name()}'s turn...")
            print("1. Attack\n2. Special Move")
            try:
                action = int(input(f"Choose action for {attacker.get_name()}: "))
                if action == 1:
                    result = attacker.attack(opponent)
                    print(result)
                elif action == 2:
                    result = attacker.special_move(opponent)
                    print(result)
                else:
                    print("Invalid choice! Using basic attack.")
                    result = attacker.attack(opponent)
                    print(result)
            except ValueError: # if the user enters a non-integer value
                print("Invalid input! Using basic attack.")
                result = attacker.attack(opponent)
                print(result)
            
            # Check if opponent is defeated
            if opponent.get_health() <= 0:
                print(f"\n🎉 {attacker.get_name()} wins the battle!")
                break
            
            # Second creature's turn (opponent)
            print(f"\nNow {opponent.get_name()}'s turn...")
            print("1. Attack\n2. Special Move")
            try:
                action = int(input(f"Choose action for {opponent.get_name()}: "))
                if action == 1:
                    result = opponent.attack(attacker)
                    print(result)
                elif action == 2:
                    result = opponent.special_move(attacker)
                    print(result)
                else:
                    print("Invalid choice! Using basic attack.")
                    result = opponent.attack(attacker)
                    print(result)
            except ValueError: # if the user enters a non-integer value
                print("Invalid input! Using basic attack.")
                result = opponent.attack(attacker)
                print(result)
            
            # Check if attacker is defeated
            if attacker.get_health() <= 0:
                print(f"\n🎉 {opponent.get_name()} wins the battle!")
                break
            
            round_num += 1
        
        # Battle summary
        print("\n" + "=" * 50)
        print("BATTLE ENDED!")
        print(f"Final Health:")
        print(f"{attacker.get_name()}: {attacker.get_health():.1f} HP")
        print(f"{opponent.get_name()}: {opponent.get_health():.1f} HP")
        
        # Update the creature data with final health
        if attacker_type == "Dragon":
            Dragon.get_Dragon_data(Dragon())['health'] = attacker.get_health()
        elif attacker_type == "Wizard":
            Wizard.get_Wizard_data(Wizard())['health'] = attacker.get_health()
        elif attacker_type == "Elf":
            Elf.get_Elf_data(Elf())['health'] = attacker.get_health()
        
        if opponent_type == "Dragon":
            Dragon.get_Dragon_data(Dragon())['health'] = opponent.get_health()
        elif opponent_type == "Wizard":
            Wizard.get_Wizard_data(Wizard())['health'] = opponent.get_health()
        elif opponent_type == "Elf":
            Elf.get_Elf_data(Elf())['health'] = opponent.get_health()
        
    except ValueError as VE:
        print(f'Error: Please enter valid numbers only')
    except Exception as e:
        print(f'An error occurred: {e}')
