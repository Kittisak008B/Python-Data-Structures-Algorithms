'''
4)  เขียนโปรแกรมเพื่อแสดงผลตัวอักษร A และ B โดยรับ input เป็นจำนวนของตัวอักษร A และ B จากนั้นแสดงผลตัวอักษรทั้งสองตามจำนวนที่ได้รับ 
    โดย ห้ามไม่ให้มีการแสดงผลตัวอักษรเดียวกันซ้ำติดกันเกิน 2 ครั้ง และจะต้องใช้ตัวอักษรทั้งหมดให้ครบตามจำนวน เช่น
    input number of A: 5
    input number of B: 3
    output: AABABABA
    (ตัวอย่าง output ที่ผิด คือ AAABABAB)
    ถ้าไม่สามารถแสดงได้ตามเงื่อนไข ให้แสดงข้อความ error
'''

dp = {}
def dfs(n_A , n_B , conservative , word) :
    if conservative == 3 :
        return []
    if (n_A , n_B) == (0,0) :
        return [word]
    if (n_A , n_B , conservative , word) in dp : 
        return dp[(n_A , n_B , conservative , word)]
    res = []
    if n_A : # Add A
        new_conservative = conservative + 1 if len(word) > 0 and word[-1] == 'A' else 1
        res += dfs(n_A - 1 , n_B , new_conservative , word + 'A')
    if n_B : # Add B
        new_conservative = conservative + 1 if len(word) > 0 and word[-1] == 'B' else 1
        res += dfs(n_A  , n_B -1 , new_conservative , word + 'B')
    dp[(n_A , n_B , conservative , word)] = res
    return dp[(n_A , n_B , conservative , word)]

def check_input():
    while True:
        try:
            user_input = int(input('Please enter a positive number :'))
            if user_input < 0:
                print('Please enter positive number !')
            else:
                return user_input
        except :
            print('Wrong input!')
            
n_A = check_input()
n_B = check_input()
dfs(n_A , n_B , 0 , '')
if len(dp[(n_A , n_B , 0 , '')]) == 0 : 
    print('error')
else :
    print(dp[(n_A , n_B , 0 , '')][1])

''' 

                         __(n_A= 5 , n_B= 3)__          base case : if conservative == 3 return , if (0,0) -> ok use all A and B
                        /                     \
                       A                       B
                     (4,3)                    (5,2)
                    /      \                 /      \
                   AA        AB              BA      BB
                 (3,3)      (4,2)          (4,2)    (5,1) 
                 /   \        /  \           / \       /  \ 
                AAA AAB      ABA ABB       BAA BAB   BBA BBB  
                 x  (3,2)_______
                    /           \
                  AABA          AABB
                 (2,2)           (3,1)
               /       \         /    \ 
            AABAA    AABAB     AABBA  AABBB
          (1,2)       (2,1)     (2,1)    x
       /       \      /  \        / \
    AABAAA AABAAB   
      x     (1,1)
            /    \
        AABAABA  AABAABB 
        (0,1)      (1,0)
          \          /
        AABAABAB    AABAABBA
         (0,0) ok    (0,0) ok
            
'''
