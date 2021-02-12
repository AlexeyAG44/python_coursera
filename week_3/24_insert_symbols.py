#string = str(input())
#last_sim = string[-1:]
#step = 1
#if len(string) > 1:
#    while len(string) > step:
#        sub_string = string[step-1:step]
#        sub_string += "*"
#        step += 1
#        print(sub_string, end="")
#    print(last_sim)
#else:
#    print(string)

# 2ой вариант не дорабол (последнюю звездочку убрать)
string = input()
for i in range(len(string)):
    if i % 1 == 0:
        res = string[i] + "*"
        print(res, sep="", end="")
