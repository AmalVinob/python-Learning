import sys


# sys.stderr.write('this is stderr text\n')
# sys.stderr.flush()
# sys.stdout.write('this is stdout text\n')

#
# print(sys.argv) # to displlay alll the arguments

# if len(sys.argv) > 1:
#     print(sys.argv[1])

# if len(sys.argv) > 1:
#     print(float(sys.argv[1]) + 5)

def main(args):
    print(args)

main(sys.argv)