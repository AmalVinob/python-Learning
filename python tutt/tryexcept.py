f1 =open("amal.txt")
try:
    f = open("does.txt.txt")

except Exception as e:
    print(e)

finally:
    print("run this anyway!!!")
    f1.close()
    # f.close()

print("important stuff ")


# finally used to clean up
#ie if work anyway
# else oe except only one thing works...........

f1 =open("amal.txt")
try:
    f = open("does.txt")
except Exception as e:
    print(e)
else:
    print("this will run only except didnt work")

finally:
    print("run this anyway!!!")
    f1.close()
    # f.close()

print("important stuff ")