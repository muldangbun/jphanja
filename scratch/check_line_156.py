with open('kaninotokoya.JSON', 'rb') as f:
    lines = f.readlines()
    line_156 = lines[155] # 0-indexed
    print(line_156)
    print(line_156.decode('utf-8'))
