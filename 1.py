import hashlib
#hashlib를 import합니다
str1 = 'The quick brown fox jumps over the lazy dog'
str2 = 'The quick brown fox jumps over the lazy cog'

#한글자만 다르게 문자열을 선언합니다.

m = hashlib.sha256() #sha256 해시 알고리즘을 사용하는 해시 객체를 생성합니다.
m.update(str1.encode('utf-8'))#원본 텍스트를 UTF-8 인코딩으로 바이트로 변환한 후

hash1 = m.hexdigest().upper()
#16진수 문자열로 반환되며 upper()를 통해 대문자로 변환합니다.
print(f"First Text: {str1}\n")
print(f"1) Hash: {hash1}\n")
#각 구문 출력

#위와 동일
m = hashlib.sha256()
m.update(str2.encode('utf-8'))

hash2 = m.hexdigest().upper()
print(f"Second Text: {str2}\n")
print(f"2) Hash: {hash2}\n")
