def voter(age):
    if age < 18:
        raise ValueError("invalid voter")
    return "you are allowed to give vote"

try:
    print(voter(20))
    print(voter(16))

except ValueError as e:
    print(e)