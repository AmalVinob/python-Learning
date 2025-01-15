import argparse
import sys

def calc(args):
    if args.o == 'add':
        if args.x == 8:
            return args.x * args.y
        else :
            return args.x + args.y
    elif args.o == 'sub':
        return args.x - args.y

    elif args.o == 'mul':
        return args.x * args.y

    elif args.o == 'div':
        return args.x / args.y

    else :
        return "some thinng went wromg "
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x',type=float, default=1.0,help="please enter the first number, if any a hellp needed please contcat amal!!!!")

    parser.add_argument('--y',type=float, default=1.0,help="please enter the second number, if any a hellp needed please contcat amal!!!!")

    parser.add_argument('--o',type=str, default="add", help="please enter the second number, if any a hellp needed please contcat amal!!!!")

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))