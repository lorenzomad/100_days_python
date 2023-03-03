with open("./names/names.txt") as names_file:
    names = names_file.readlines()

with open("./example/example_mail.txt", "r") as mail_file:
    example_mail = mail_file.read()
    for name in names:
        stripped_name = name.strip()
        mail = example_mail.replace("[name]", stripped_name)
        with open(f"./output/mail_{stripped_name}.txt", 'w') as output_file:
            output_file.write(mail)
