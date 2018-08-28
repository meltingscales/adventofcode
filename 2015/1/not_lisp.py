nmap = {
    '(': 1,
    ')': -1
}

unique_pos = {}

with open('input', 'r') as f:
    s = f.read()

    x = 0
    i = 1

    for char in s:
        x += nmap[char]

        if x not in unique_pos:
            unique_pos[x] = (char, i)
        
        print((" "*x) + char)
        i += 1

print(x)
print(unique_pos[-1])
