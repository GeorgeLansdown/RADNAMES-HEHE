def generate(name):
	name = name.split(" ")
	newName = ""
	for n in name:
		if n.split("-") != n:
			for f in n.split("-"):
				if f[0].lower() not in ['a','e','i','o','u']:
					newName += f[0]
				newName += "onk "
		else:
			if n[0].lower() not in ['a','e','i','o','u']:
				newName += n[0]
				newName += "onk "
	return newName

names = []
for line in open('names', 'r').readlines():
	if line.strip() == '':
		continue
	names.append(line)

for n in names:
	print(n  + generate(n))
