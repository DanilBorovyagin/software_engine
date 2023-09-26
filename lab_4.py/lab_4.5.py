def main (**kwargs):
    for i in kwargs.items():
        print(i[0], i[1])

    print()

    for key in kwargs:
        print(f"{key} = {kwargs[key]}")


if __name__ == "__main__":
    main(x = [1,2,3], y=[44,4,0], z=[4,44,444,4444])
    print()
    main(**{"x": [4,44,444]})