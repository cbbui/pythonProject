
import argparse
import sys

def f1(args):
    if args.o=="add":
        return args.x+args.y

    elif args.o=="sub":
        return args.x-args.y

    elif args.o=="mul":
        return args.x*args.y

    elif args.o=="div":
        return args.x/args.y

    elif args.o=="mod":
        return args.x%args.y

    else:
        return "Something went Wrong"

if __name__ == '__main__':

 a=argparse.ArgumentParser()
 a.add_argument('--x', type=float, default=2.0, help="CONTACT MUSKAN")

a.add_argument('--y', type=float, default=4.0, help="CONTACT MUSKAN")

a.add_argument('--o', type=str, default="add", help="CONTACT MUSKAN")

args=a.parse_args()

sys.stdout.write(str(f1(args)))

