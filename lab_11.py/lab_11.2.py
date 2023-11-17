class Count:
    def __init__(self, start):
        self.Count = start + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.Count -= 1
        if self.Count < 0:
            raise StopIteration
        return self.Count


user = int(input("введите число "))

counter = Count(user)

for i in counter:
    print(i)
