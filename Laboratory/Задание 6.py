scores = {"Alice": 85, "Bob": 90}
scores["Charlie"] = 78
print(scores)
scores["Bob"] = 95
print(scores)
dave_score = scores.get("Dave", "не найден")
print("Dave: {dave_score}")
removed_score = scores.pop("Alice")
print(scores)
print( len(scores))
print(list(scores.keys()))
print(list(scores.values()))
