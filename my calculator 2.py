#simple calculator
import time
Active = True
while Active:
    print("my first calculator")
    try:
        num1 = float(input("enter first number : "))
    except ValueError:
        print('Input Numbers Only')
        continue
    else:
        try:
            num2=float(input("enter second number : "))
        except ValueError:
            print('Input Numbers Only')
            continue
        else:
            print("Operator choose:\n\t1. Plus\n\t2. Minus\n\t3. Multiply\n\t4. Divided\n\t5. Percentage\n\t6. Quit")
            op_list = (1,2,3,4,5,6)
            try:
                op=float(input())
            except ValueError:
                print('Input Numbers Only')
                continue
            else:
                if op not in op_list:
                    print("Error ! please check your Operators")
                    continue
                else:
                    if op==1:
                        print(num1,"+",num2,"=",num1+num2)
                    elif op==2:
                        print(num1,"-",num2,"=",num1-num2)
                    elif op==3:
                        print(num1,"*",num2,"=",num1*num2)
                    elif op==4:
                        try:
                            print(num1,"/",num2,"=",num1/num2)
                        except ZeroDivisionError:
                            print(num1, '/',num2,'(Math Error)')
                            continue                    
                    elif op==5:
                        xx=num2/100*num1
                        print(num1,"%",num2,"=",num1-xx)
                    elif op == 6:
                        print()
                        print()
                        time.sleep(0.4)
                        print("               ধন্যবাদ আপনার দিনটি শুভ হোক")
                        Active = False
