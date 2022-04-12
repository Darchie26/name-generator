import sys, random

print("Welcome to Baby Name Generator. '\n")
print("A special name for your Baby:\n\n")

first = ('Karsyn', 'Olivia','Aniya', 'Emma', 'Ava', 'Charlotte', 'Sophia', 'Amelia', 'Isabella', 'Mia', 'Evelyn', 'Harper','Willow','Isla','Freya','Mila','Evie','lilly','Grace','Aaliyah','Amara','Kyle','Jade')

middle = ('Elizabeth', 'Violet', 'Josephine', 'Maeve', 'Wren', 'Mae', 'Claire', 'Briar', 'Blythe', 'Arden', 'Nyx', 'Scout', 'Ruth', 'Mary', 'Indigo', 'Avalon', 'Arya', 'Anne', 'Arcadia', 'Zephyr', 'Reign', 'Fleur' )

last = ('Archie', 'Johnson')
while True:
    firstName = random.choice(first)
    middleName = random.choice(middle)
    lastName = random.choice(last)


    print("\n\n")
    print("{} {} {}".format(firstName, middleName, lastName), file=sys.stderr)
    print("\n\n")

    try_again = input("\n\nTry again? (Press Enter else n to quit)\n")

    input("\nPress Enter to exit.")