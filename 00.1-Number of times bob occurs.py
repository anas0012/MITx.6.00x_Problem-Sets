string_Example = 'azcbobobegghakl'
name = 'bob'
count = 0
n = 0

while (0 <= n < len(string_Example)):
    try:
        for letter in string_Example:
            if string_Example[n] == 'b':
                if string_Example[n+1] == 'o':
                    if string_Example[n+2] == 'b':
                        count += 1
            n += 1
    except:
        break

    
print('Number of times bob occurs is: ', count)