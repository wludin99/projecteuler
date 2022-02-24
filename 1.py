cap = 1000
threes = [i for i in range(cap) if i % 3 == 0]
fives = [i for i in range(cap) if i % 5 == 0]
print(sum(threes))
print(sum(fives))
all = set(threes) | set(fives)
print(sum(all))
