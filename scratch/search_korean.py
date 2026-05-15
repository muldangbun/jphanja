import json

with open('kaninotokoya.JSON', 'r', encoding='utf-8') as f:
    text = f.read()

if '부터' in text:
    print("FOUND '부터' in file")
else:
    print("NOT FOUND '부터' in file")

if '까지' in text:
    print("FOUND '까지' in file")

if '하지만' in text:
    print("FOUND '하지만' in file")
