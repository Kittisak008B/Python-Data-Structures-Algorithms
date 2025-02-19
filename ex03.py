'''
3)  เขียนโปรแกรมเพื่อแสดงรูปแบบตามที่กำหนด โดยรับ input เป็นขนาดของ pattern เป็นจำนวนคี่ และแสดงผลเป็น pattern ที่สัมพันธ์กับขนาดที่ได้รับ เช่น
    Input              Output
    
      3                *-*
                       -*-
                       *-*
                       
      5                *---*
                       -*-*-
                       --*--
                       -*-*-
                       *---*
                       
      7                *-----*
                       -*---*-
                       --*-*--
                       ---*---
                       --*-*--
                       -*---*-
                       *-----*
'''
def check_input():
    while True:
        try:
            user_input = int(input('Please enter a positive odd number :'))
            if user_input <= 0:
                print('Please enter a positive odd number !')
            elif user_input % 2 == 0 :
                print('Please enter a positive odd number !')
            else:
                return user_input
        except :
            print('Wrong input!')

def make_pattern(n) :
    for row in range(n) :
        for col in range(n) :
            if row == col or col == n - row - 1 :
                print('*' , end = '') # print(end='\n') provides new line after printing   , end='' -> no new line
            else :
                print('-' , end = '')
        print()
            
user_input = check_input()
make_pattern(user_input)
