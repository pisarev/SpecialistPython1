j = 0
fruit: str
for fruit in fruits:
    k = len(fruit);
    if j < k: j = k

i = 1
for fruit in fruits:
    print(f"# {i}.{fruit:>{j + 1}}")
    i += 1
