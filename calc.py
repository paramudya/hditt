lst_of_depressing_w=['sad', 'sick of', 'fuck it','fuck that','fuck it',':(']
input_sent='So sad of this, fuck it'

def hard_code(stringg):
    count_depress=0
    for word in lst_of_depressing_w:
        if word.lower() in stringg.lower():
            count_depress+=1
    return round(count_depress/len(input_sent.split())*100,2)

# if __name__ == '__main__':
#     n = int(input("number of test cases: "))
#     ints = list(map(int,input("insert {} integer{} each separated with space:\n".format(n,'' if n <= 1 else 's')).split()))

#     try:
#         for i in range(n):
#             print(nine(ints[i]))
#     except:
#         print("number of integers you just put in is less than what you said earlier!")