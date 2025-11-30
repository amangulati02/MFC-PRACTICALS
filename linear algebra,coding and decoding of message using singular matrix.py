import numpy as np

def encode(message, key):
    message = message.upper().replace(" ", "")
    nums = [ord(c) - 64 for c in message]

    while len(nums) % 3 != 0:
        nums.append(0)

    nums = np.array(nums).reshape(-1, 3)
    coded = nums.dot(key)
    return coded

def decode(coded, key):
    key_inv = np.linalg.inv(key)
    nums = coded.dot(key_inv).flatten()
    text = ""

    for n in nums:
        n = round(n)
        if 1 <= n <= 26:
            text += chr(n + 64)
        else:
            text += " "

    return text.strip()

message = "LINEAR ALGEBRA IS FUN"
key = np.array([[2, 3, 1],
                [1, 1, 1],
                [1, 2, 2]])

print("Original Message:", message)

coded = encode(message, key)
print("\nEncoded Matrix:\n", np.round(coded))

decoded = decode(coded, key)
print("\nDecoded Message:", decoded)
