import re
pattern = r"colour"
if re.search(pattern,"RED IS A colour, i love red"):
    print("Match")
else:
    print("Not matched")