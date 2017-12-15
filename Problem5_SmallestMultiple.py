'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
answer = 20*10
answer_found = False

while (answer_found == False and answer <= (2*3*4*5*6*7*8*9*10*11*12*13*14*15*16*17*18*19*20)):
    print ("try " + str(answer))
    print ("max " + str(2*3*4*5*6*7*8*9*10*11*12*13*14*15*16*17*18*19*20))
    if (answer%1 ==0 and answer%2==0 and answer%3==0 and answer%4==0 and answer%5==0):
        if(answer%6==0 and answer%7==0 and answer%8==0 and answer%9==0 and answer%10==0):
            if(answer%11==0 and answer%12==0 and answer%13==0 and answer%14==0 and answer%15==0):
                if(answer%16==0 and answer%17==0 and answer%18==0 and answer%19==0 and answer%20==0):
                    answer_found = True
    if not(answer_found):
        answer += 20
print (answer)
