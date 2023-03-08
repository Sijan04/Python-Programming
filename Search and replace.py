import re
pattern = r"colour"
text1 = "My fav colour is red"
text2 = re.sub(pattern,"color",text1,count=1)
print(text2) 