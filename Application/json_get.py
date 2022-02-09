import json

# オブジェクトからJSON文字列へ変換
json_data = {'Python': 'python-izm.com',
             'SearchEngline': ('google.co.jp', 'yahoo.co.jp')}

print(type(json_data))

encode_json_data = json.dumps(json_data, indent=4)

print(encode_json_data)
print(type(encode_json_data))

# JSON文字列からオブジェクトへ変換
decode_json_data = json.loads(encode_json_data)
print(decode_json_data)
print(type(decode_json_data))
