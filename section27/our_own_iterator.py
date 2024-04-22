class Counter:
    def __init__(self, low, high) -> None:
        self.current = low
        self.max = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max:
            num = self.current
            self.current += 1
            return num
        raise StopIteration


c = Counter(0, 19)

for i in c:
    print(i)
