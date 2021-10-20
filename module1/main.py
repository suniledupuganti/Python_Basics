# zfill function will fill the zeros till it has number
account_num = '10'
print(account_num.zfill(16))

name = "Sunil is Super"
print(name.find('u'))
print(name.index('u'))
# Difference between find and index is:
# When we find a character which is not present find will give the output as -1 but index will throw the error

# Counts the specific character in a String
print(name.count('S'))

print(name.replace('Super', 'great'))

# Split converts the string to ARRAY
print(name.split())

if "is" in name:
    print("Hello")

