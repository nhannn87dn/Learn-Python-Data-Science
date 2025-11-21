# file = open('./Day-07/tutorials/demo.txt', 'rt', encoding="utf-8")
# content = file.read()
# print(content)
# file.close()
with open('./Day-07/tutorials/write.txt', 'rt', encoding="utf-8") as f:
    print(f.read())
