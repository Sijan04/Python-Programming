import  re
pattern = r"[aeiou]"

if re.match(pattern,"a"):
    print("matched")

else:
    print("not matched")