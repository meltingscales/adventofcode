import hashlib
import os
from joblib import Memory

memory = Memory(cachedir=
                os.path.join(os.path.dirname(__file__), '__pycache__'),
                verbose=0)


def generate_key(data, it=0):
    return data + str(abs(it) + 1)


@memory.cache
def try_generate_hash(data, zeroes=5):
    i = 0
    while True:
        mod_data = generate_key(data, i)  # Generate key
        h = hashlib.md5(mod_data.encode("utf-8")) # generate hash from key
        h2 = h.hexdigest() # turn binary into ascii '1234567890ABCDEF'

        print(f"{mod_data} -> {h2}") # key -> hash

        if h2[0:zeroes] == ('0' * zeroes): # if it contains sufficient zeroes
            print("Success!") # :-)
            return (mod_data, h2)

        i += 1


with open('input', 'r') as f:
    data = f.readlines()[0]

vh1 = try_generate_hash(data, 5)
vh2 = try_generate_hash(data, 6)

print("Valid hash:")
print(vh1)

print("Valider hash:")
print(vh2)
