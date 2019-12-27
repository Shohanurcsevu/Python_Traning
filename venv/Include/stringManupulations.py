# str  = "shohan"
# print(type(str))
# print(len(str))
# print(str)
# s = reversed(str)
# print(s)
#
# def rev(str):
#     strf="".join(reversed(str))
#     return strf
#
# str1='shohan'
# stro = rev(str1)
# print(stro)

# str = []
# # sto = []
# # str1= 'Shohan'
# # print(type(str))
# #
# # for i in range(5,1,-1):
# #     str.append(str1[i])
# #     print(str)
# #
# #
# # for j in range (len(str),0,-1):
# #     sto.append(str[j])
# #
# # print(sto)

str = input()
strl = []
# print(len(str))
for i in range(len(str)):
     strl.append(str[i])
n=len(strl)
print(str)
for j in range(len(strl)-1,-1,-1):
    k=strl.index(strl[j])
    print(strl[k],end= '')

# for i in range(10,-1,-1):
#     print(i)

