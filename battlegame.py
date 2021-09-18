wizard = 'Wizard'
elf = 'Elf'
human = 'Human'
orc = 'Orc'

wizard_hp = 70
elf_hp = 100
human_hp = 150
dragon_hp = 300
orc_hp = 370

wizard_damage = 150
elf_damage = 100
human_damage = 20
dragon_damage = 50
orc_damage = 35

is_playing = True
while is_playing == True:
    while is_playing == True:
        print("1)   Wizard\n2)   Elf\n3)   Human\n4)   Orc\n5)   Exit")
        character = input("Choose your character: ").lower()
        if character == '1' or character == 'wizard':
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            print(f"You chose {character}\n")
            print(f"Health: {my_hp}")
            print(f"Damage: {my_damage}\n")
            break

        elif character == '2' or character == 'elf':
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            print(f"You chose {character}\n")
            print(f"Health: {my_hp}")
            print(f"Damage: {my_damage}\n")
            break

        elif character == '3' or character == 'human':
            character = human
            my_hp = human_hp
            my_damage = human_damage
            print(f"You chose {character}\n")
            print(f"Health: {my_hp}")
            print(f"Damage: {my_damage}\n")
            break

        elif character == '4' or character == 'orc':
            character = orc
            my_hp = orc_hp
            my_damage = orc_damage
            print(f"You chose {character}\n")
            print(f"Health: {my_hp}")
            print(f"Damage: {my_damage}\n")
            break

        elif character == '5' or character == 'exit':
            is_playing = False
            print('Bye!')
            break

        else:
            print("Unknown character")

    while is_playing == True:

        dragon_hp -= my_damage
        print("The", character, "damaged the Dragon!")
        if dragon_hp <= 0:
            print("The dragon lost the battle!")
            break
        my_hp -= dragon_damage
        print("The", character, "has been damaged and has", my_hp, "hp left\n")
        if my_hp <= 0:
            print("The", character, "lost the battle")
            break
    choice = input("Play again? y or n? ").lower()
    wizard_hp = 70
    elf_hp = 100
    human_hp = 150
    dragon_hp = 300
    orc_hp = 370

    if choice == 'n':
        is_playing = False
