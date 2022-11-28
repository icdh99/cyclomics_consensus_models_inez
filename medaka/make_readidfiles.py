with open('name.txt') as f:
    lines = f.read().splitlines()
    print(lines)
    print(len(lines))

for name in lines:
    with open(f'txtfiles/{name}.txt', 'w') as f:
        f.write(name)
        f.write('\n')
