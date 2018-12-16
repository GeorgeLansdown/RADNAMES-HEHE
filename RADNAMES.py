def generate(name):
	name = name.split(" ")
	newName = ""
	for n in name:
		if n[0].lower() not in ['a','e','i','o','u']:
			newName += n[0]
		newName += "onk "
	return newName

names = ["Michael Aylesbury", "George Lansdown", "Jen Logan", "Liana Ahmed", "Jacob Rees Mog", "Orla Innes"]
for f in names:
	print f, generate(f)
		
