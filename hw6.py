while True:
 num=int(input("원하는 구구단은 몇단인가요:"))
# while n<=9 :
#     print(num,"*",n,"=",num*n)
#     n+=1
 for x in range(1,10):
    mul=num*x
    print(num,"*",x,"=",mul)
 q=input("프로그램을 종료하려면  q,계속하려면 아무키나 눌러 주세요 ")
 if q=="q" :
    break
