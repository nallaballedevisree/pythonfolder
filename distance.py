def string_distance(str1, str2):
    max_len=max(len(str1),len(str2))
    str1=str1(max_len)
    str2=str2(max_len)
    
    distance = 0
    for char1, char2 in zip(str1, str2):
        distance += abs(ord(char1) - ord(char2))
    
    return distance

str1 = "hello"
str2 = "hxllo"
distance = string_distance(str1, str2)
print(f"The ASCII distance between '{str1}' and '{str2}' is {distance}.")