def main(x, y, z, *args):
    one = x
    xac = y
    xac1 = z
    ron = xac**2
    ron1 = xac1*2
    two = sum(args)
    three = float(len(args))
    test = args[7] + args[6] / args[0]

    print(f"one={one}\ntwo={two}\nthree={three}\nfour={ron}\nfive={ron1}")

    return (x + sum(args) / float(len(args)) - y ** z) / (test)


if __name__ == "__main__":

    res = int(main(4, 44,2,2,3,4,5,6,1,-10,22))

    print(f"result={res}")
