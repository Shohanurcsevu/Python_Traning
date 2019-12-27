def mycopy(s1,s2):
    for i in range(len(s1)):
        s2 = s2+s1[i]

    return s2



s1='pkoj;iuilktyhbxrd'
s2=''

s3 = mycopy(s1,s2)
print(s3)
# str1 = "Please Enter Your Own String : "
# str2 = ''
#
# for i in range(len(str1)):
#     str2 = str2 + str1[i]
#
# print("The Final String : Str2  = ", str2)