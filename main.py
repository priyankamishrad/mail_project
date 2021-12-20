PLACEHOLDER = "[name]"

with open('invited_names.txt', mode='r') as names_file:
    names = names_file.readlines()
    stripped = [s.strip() for s in names]

with open('starting_letter.txt', mode='r') as letter_file:
    letter = letter_file.read()
    for name in stripped:
        new_letter = letter.replace(PLACEHOLDER, name)
        with open(f"Output/letter_for_{name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
