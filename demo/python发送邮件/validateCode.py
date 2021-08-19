import random
def generate_verification_code():

    ''' 随机生成6位的验证码 '''

    code_list = []

    for i in range(10): # 0-9数字

        code_list.append(str(i))

    for i in range(65, 91): # A-Z

        code_list.append(chr(i))

    for i in range(97, 123): # a-z

        code_list.append(chr(i))
    myslice = random.sample(code_list, 6)  # 从list中随机获取6个元素，作为一个片断返回

    verification_code = ''.join(myslice) # list to string

    # print code_list

    # print type(myslice)

    return verification_code
def generate_verification_code2():

    ''' 随机生成6位的验证码 '''

    code_list = []

    for i in range(2):

        random_num = random.randint(0, 9) # 随机生成0-9的数字

        # 利用random.randint()函数生成一个随机整数a，使得65<=a<=90

        # 对应从“A”到“Z”的ASCII码

        a = random.randint(65, 90)

        b = random.randint(97, 122)

        random_uppercase_letter = chr(a)

        random_lowercase_letter = chr(b)
        code_list.append(str(random_num))

        code_list.append(random_uppercase_letter)

        code_list.append(random_lowercase_letter)

    verification_code = ''.join(code_list)

    return verification_code
if __name__ == '__main__':

    code = generate_verification_code()

    code2 = generate_verification_code2()

    print(code)

    print(code2)