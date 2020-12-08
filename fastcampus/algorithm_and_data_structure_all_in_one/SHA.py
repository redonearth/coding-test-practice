# 참고: 해시 함수와 키 생성 함수
# 파이썬의 hash() 함수는 실행할 때마다 값이 달라질 수 있다.
# 유명한 해시 함수: SHA(Secure Hash Algorithm, 안전한 해시 알고리즘)
# 어떤 데이터라도 유일한 고정된 크기의 고정값을 리턴해주므로, 해시 함수로 유용하게 활용 가능하다.

import hashlib

data = 'test'.encode()  # b'test' 이렇게도 쓸 수 있다.

# SHA-1
hash_object = hashlib.sha1()
hash_object.update(data)
hex_dig = hash_object.hexdigest()

print('SHA-1:', hex_dig)

# SHA-256
hash_object2 = hashlib.sha256()
hash_object2.update(data)
hex_dig2 = hash_object2.hexdigest()

print('SHA-256:', hex_dig2)
