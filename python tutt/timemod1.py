import time
import datetime

# initial = time.time()
# print(initial)
#
# k=0
# while k<50000:
#     print("this is amal")
#     time.sleep(2)
#     k+=1
# print(time.time() - initial)
#
# initial2 = time.time()
# for i in range(45):
#     print("this is harry bhai")
# print(time.time() - initial)



# locale = time.asctime()
#
# print(locale)
#
# locate = time.asctime(time.localtime(time.time()))
#
# print(locate)

#
# seconds = time.ctime()
#
# print("Seconds since epoch =", seconds)
#
# time.sleep(2)
# print("this will print after 2 ssecond")
#
# result = time.localtime(1545925769)
# print("result:", result)
# print("\nyear:", result.tm_year)
# print("tm_hour:", result.tm_hour)


localtime = time.asctime(time.localtime(time.time()))
print(localtime)
ltime = datetime.datetime.now()
print(ltime)

if time.localtime().tm_hour >= 9:
    print("hi")