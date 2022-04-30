#讀test.txt的檔案, 寫入data
data = []
with open('test.txt', 'r') as zoo:
	for animal in zoo:
		data.append(animal.strip())
print(data)