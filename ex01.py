'''
1)  เขียนโปรแกรมเพื่อรับ input เป็น string และแสดงผลเป็น string นั้นในลำดับที่กลับกัน เช่น
    input: HELLO
    output: OLLEH
'''
def reverse_string(word) :
    s = [char for char in word]
    i = 0
    j = len(s) - 1
    while i < j :
        s[i] , s[j] = s[j] , s[i]
        i += 1
        j -= 1
    return ''.join(s)
    
user_input = input('Please enter a string : ')
print(reverse_string(user_input))


# a= 'hello  a'
# print(a[::-1])
