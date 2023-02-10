def makeDic(list):
	dic = {}
	for key, value in list:
		if key in [x for x in dic.keys()]:
			dic[key] = [dic[key], value]
		else:
			dic[key] = value
		
	return dic

print(makeDic([('hi', 'something'), ('hi', 'nothing'), ('good', 'day')]))