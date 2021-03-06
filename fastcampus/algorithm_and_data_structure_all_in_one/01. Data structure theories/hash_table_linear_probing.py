# Linear Probing 기법
# 폐쇄 해싱 또는 Closing Hashing 기법 중 하나
# 충돌이 발생하면, 해당 hash address의 다음 address부터 가장 처음으로 나오는 빈 공간에 저장하는 기법
# 저장 공간 활용도를 높이기 위한 기법

import hashlib

hash_table = list([0 for i in range(8)])


def get_key(data):
    hash_object = hashlib.sha256()
    hash_object.update(data.encode())
    hex_dig = hash_object.hexdigest()
    return int(hex_dig, 16)  # 16진수의 문자열을 10진수로 변환


def hash_function(key):
    return key % 8


def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                hash_table[index] = [index_key, value]
                return
            elif hash_table[index][0] == index_key:
                hash_table[index][1] = value
                return
    else:
        hash_table[hash_address] = [index_key, value]


def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                return None
            elif hash_table[index][0] == index_key:
                return hash_table[index][1]
    else:
        return None


save_data('Dave', 'Chief')
save_data('Chris', 'Soldier')
save_data('Redonearth', 'Programmer')

print(read_data('Dave'))
print(read_data('Chris'))
print(read_data('Redonearth'))
