import re
pattern = r"ice(-)?cream"

if re.match(pattern,"ice-cream"):
    print("matched")
else:
    print("not matched")