class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.cookies = 0

    def __str__(self):
        return str(self.cookies)

    def deposit(self, n):
        self.cookies += n
        if self.cookies > self.capacity:
            raise ValueError("Jar is full.")
        return self.cookies

    def withdraw(self, n):
        self.cookies -= n
        if self.cookies < 0:
            raise ValueError("There aren't that much cookies in the jar.")

    # Getter
    @property
    def capacity(self):
        return self._capacity

    # Setter
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Invalid capacity")
        self._capacity = capacity

    # Getter
    @property
    def size(self):
        return self.cookies

    # Setter
    # @size.setter
    # def size(self, size):
