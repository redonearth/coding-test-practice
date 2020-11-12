hash_table = list([i for i in range(10)])


def hash_func(key):
    return key % 5


def storage_data(data, value):
    key = ord(data[0])
    # ord(): 문자의 ASCII(아스키) 코드 리턴
    hash_address = hash_func(key)
    hash_table[hash_address] = value


data = 'Redonearth'

storage_data(data, 'https://redonearth.com')


def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]


print(get_data(data))
