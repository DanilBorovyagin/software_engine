def main(**kwargs):

    for i, j in kwargs.items():
        print(f"{i}. среднее арифметическое = {mean(j)}")


def mean(da):

    return sum(da) / float(len(da))


if __name__ == "__main__":

    main(x=[4,44,444], y = [4,44,44,444,44,44,4])
