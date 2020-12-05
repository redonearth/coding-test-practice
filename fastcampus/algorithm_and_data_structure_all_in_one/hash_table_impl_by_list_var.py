hash_table = list([0 for i in range(8)])


def get_key(data):
    return hash(data)


def hash_function(key):
    return key % 8


def save_data(data, value):
    hash_address = hash_function(get_key(data))
    hash_table[hash_address] = value


def read_data(data):
    hash_address = hash_function(get_key(data))
    return hash_table[hash_address]


save_data('Redonearth', '01010001000')
save_data('Koongdori', '01020002000')

print(read_data('Redonearth'))
print(hash_table)
