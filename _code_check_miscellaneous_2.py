# from os.path import realpath, relpath
# from os import chdir, getcwd
#
# path = "C:\\Users\\Holly Lord\\Desktop\\Steam.lnk"
#
# real_path = realpath(path)
# print(real_path)
# chdir('C:')
# real_path = relpath(path)
# print(real_path)
# print(getcwd())

with open('C:\\Users\\Holly Lord\\Desktop\\Gomoku+.bat', 'r') as f:
    content = f.read()

print(content)

content_line = content.split('\n')
print(content_line)
palindrome = []

for element in content_line:
    word_list = element.split(' ')
    for word in word_list:
        print(word)
        if word == word[::-1]:
            palindrome.append(word)

print(palindrome)

string1 = "Padding"
string2 = "hahahahhahah"
print(f"{string1:0^32} This")
print(f"{string2:<32} This")

