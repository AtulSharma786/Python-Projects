import re

str = '''E:\Windows Files\Python37\python.exe" "C:/Users/AV Sharma/PycharmProjects/projectdb/060-Regular Expression.py"
        Traceback (most recent call last):
        File "C:/Users/AV Sharma/PycharmProjects/projectdb/060-Regular Expression.py", line 2, in <module>
        fdg
        NameError: name 'fdg' is not defined
        Process finished with exit code 1'''

# findall, search, split, sub, finditer

path = re.compile(r'name')
path = re.compile(r'.adm')
path = re.compile(r'e$')

path = re.compile(r'ex*')

matches = path.finditer(str)

for match in matches:
    print(match)
    print(str[232:236])
