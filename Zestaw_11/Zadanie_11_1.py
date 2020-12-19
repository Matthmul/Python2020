import random
import numpy as np


class RandomListNumbers:
    def __init__(self, size=10):
        self.size = size
        self.int_number_list = list(range(0, self.size))

    def rand_numbers(self):
        random.shuffle(self.int_number_list)
        return self.int_number_list

    def rand_sorted_numbers(self):
        self.int_number_list = list()
        sorted_number_list = list(range(self.size, 0, -1))
        for i in range(0, self.size):
            rand = random.randint(0, 2)
            if rand == 0:
                rand = random.choice(sorted_number_list)
                self.int_number_list.append(rand)
                sorted_number_list.remove(rand)
            else:
                self.int_number_list.append(sorted_number_list.pop())
        return self.int_number_list

    def rand_sorted_numbers_rev(self):
        self.rand_sorted_numbers()
        self.int_number_list.reverse()
        return self.int_number_list

    def float_gauss(self):
        mu, sigma = 0, 1
        float_number_list = np.random.normal(mu, sigma, self.size)
        return float_number_list

    def rand_duplicate_numbers(self):
        int_duplicated_number_list = np.random.choice(self.size, self.size, replace=True)
        return int_duplicated_number_list


if __name__ == "__main__":
    listNumbers = RandomListNumbers()

    print("a)")
    print(listNumbers.rand_numbers())

    print("b)")
    print(listNumbers.rand_sorted_numbers())

    print("c)")
    print(listNumbers.rand_sorted_numbers_rev())

    print("d)")
    print(listNumbers.float_gauss())

    print("e)")
    print(listNumbers.rand_duplicate_numbers())
