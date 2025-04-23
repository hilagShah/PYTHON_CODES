name = input("Enter full name: ")
phone = input("Enter phone number: ")
email = input("Enter email address (optional): ")
address = input("Enter address (optional): ")
filename = input("Enter file name to save (e.g., contact.vcf): ")


vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL;TYPE=CELL:{phone}
EMAIL:{email}
ADR;TYPE=HOME:;;{address}
END:VCARD
"""

# Writing vCard to file
with open(filename, 'w') as f:
    f.write(vcard)

print(f"vCard saved successfully as '{filename}'. You can now import it to your mobile.")
