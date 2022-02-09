import hashlib
import uuid


# md5, sha1でのハッシュ化　引数はバイト列
print(hashlib.md5(b'python-izm').hexdigest())
print(hashlib.sha1(b'python-izm').hexdigest())

# UUIDの生成  uuid4はランダムにUUIDの生成をする
print(uuid.uuid4())
