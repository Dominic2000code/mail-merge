starting_letter_location = './Input/Letters/starting_letter.txt'
names_location = "./Input/Names/invited_names.txt"
ready_to_send_location = "./Output/ReadyToSend"

names = []
letter_template_str = ""

with open(names_location) as invited_names:
    for name in invited_names.readlines():
        names.append(name.strip())

with open(starting_letter_location) as letter_template:
    letter_template_str = letter_template.read()

for name in names:
    with open(ready_to_send_location + f"/letter_for_{name}.txt", mode="w") as output_letter:
        output_letter.write(letter_template_str.replace("[name]", f"{name}"))
