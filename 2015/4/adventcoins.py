import hashlib


def valid_hash(hash: str):
    """Are the first 5 chars all zeroes?"""
    return (hash[0:5] == '00000')


def generate_key(data, it=0):
    return data + str(abs(it) + 1)


def try_generate_hash(data, max=100):
    for i in range(0, max):
        mod_data = generate_key(data, i)  # Generate key
        h = hashlib.md5(mod_data.encode("utf-8"))
        h2 = h.hexdigest()

        print(f"{mod_data} -> {h2}")

        if valid_hash(h2):
            print("Success!")
            return h2


with open('input', 'r') as f:
    data = f.readlines()[0]

try_generate_hash(data, 999999999)
