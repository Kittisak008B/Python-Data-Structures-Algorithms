'''
2)  เขียนโปรแกรมเพื่อคำนวณลำดับฟิโบนัคชี (Fibonacci) โดยรับ input เป็นจำนวนของลำดับและแสดงผลตามจำนวนนั้น (เริ่มนับจาก 0) เช่น
    input: 5
    output: 0, 1, 1, 2, 3
    หมายเหตุ 
    (1) ลำดับฟิโบนัคชีสามารถคำนวณได้จากสูตร Fn = Fn-1 + Fn-2 โดย F0 = 0 และ F1 = 1
    (2) ข้อนี้มีคะแนนพิเศษสำหรับการเขียนโปรแกรมแบบ recursive function
'''
dp = {0:0 , 1:1}  
def fibo(n) :
    if n in dp :
        return dp[n]
    dp[n] = fibo(n-1) + fibo(n-2)
    return dp[n]

def print_sequence() :
    res = ''
    for i in range(len(dp) - 1) :
        res += str(dp[i]) + ', '
    print(res[:-2])

def check_input():
    while True:
        try:
            user_input = int(input('Please enter fibonacci sequence : '))
            if user_input <= 0:
                print('Please enter a positive number !')
            else:
                return user_input
        except :
            print('Wrong input!')
            
user_input = check_input()
fibo(user_input)
print_sequence()
