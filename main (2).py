import random

placeholder = "{name}"

with open("C:\\Users\\hp\\Documents\\Python Dev Udemy\\Mail Merge\\invite.txt") as inv:
    names = inv.readlines()
    print(names)

with open("C:\\Users\\hp\\Documents\\Python Dev Udemy\\Mail Merge\\format.txt") as frmt:
    formats = frmt.read()

    for name in names:
        stripped = name.strip()
        new = formats.replace(placeholder,stripped)
        print(new)
        with open(f"C:\\Users\\hp\\Documents\\Python Dev Udemy\\Mail Merge\\letter_for_{name}.txt", "w") as completed:
            completed.write(new)