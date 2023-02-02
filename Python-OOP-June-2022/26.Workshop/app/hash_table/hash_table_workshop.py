class HashTable:
    DEFAULT_CAPACITY = 4

    def __init__(self):
        self.data = [None] * self.DEFAULT_CAPACITY
        self.free_slots = self.DEFAULT_CAPACITY

    def add(self, key, value):
        if self.free_slots == 0:
            self.double_slots()

        index = self.calc_index(key)
        if self.data[index] is None:
            self.data[index] = [(key, value)]
            self.free_slots -= 1
            return

        for k, v in self.data[index]:
            if k == key:
                raise KeyError

        self.data[index].append((key, value))

    def get(self, key):
        index = self.calc_index(key)
        elements = self.data[index]

        if elements is None:
            raise KeyError(f"{key} not found")

        for k, v in elements:
            if k == key:
                return v

        raise KeyError(f"{key} not found")

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        try:
            old_value = self.get(key)
            idx = self.calc_index(key)
            self.data[idx].remove((key, old_value))
            self.data[idx].append((key, value))
        except KeyError:
            self.add(key, value)

    def calc_index(self, key):
        return hash(key) % len(self.data)

    def remove(self, key):
        index = self.calc_index(key)
        elements = self.data[index]

        if elements is None:
            raise KeyError(f"{key} does not exist")

        for k, v in elements:
            if k == key:
                self.data.remove((k, v))
                return

        raise KeyError(f"{key} does not exist")

    def double_slots(self):
        extend_capacity = len(self.data) * 2
        existing_data = self.data.copy()

        self.free_slots = extend_capacity

        self.data = [None] * self.free_slots

        for slot in existing_data:
            for key, value in slot:
                self.add(key, value)

    def __len__(self):
        return sum([len(key) for key in self.data if key is not None])

    def items(self):
        result = []
        for slot in self.data:
            if slot is None:
                continue
            result.extend([(k, v) for k, v in slot])
        return result


ht = HashTable()
ht.add("Pesho", 10)
ht.add("Gosho", 11)
ht.add("Jivko", 22)
ht.add("Misho", 13)
ht.add("Ivan", 14)
ht.add("Ivan2", 14)
ht.add("Ivan3", 14)
ht.add("Ivan4", 14)
print(ht.data)
print(ht.get('Misho'))
print(len(ht))
print(ht.items())
