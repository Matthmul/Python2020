import matplotlib.pyplot as plt
import matplotlib.animation as animation

from Zestaw_11.Zadanie_11_1 import RandomListNumbers

def swap(L, left, right):
    """Zamiana miejscami dwóch elementów na liście."""
    item = L[left]
    L[left] = L[right]
    L[right] = item


def bubblesort(L, left, right, filename):
    fig = plt.figure()
    ims = []

    for i in range(left, right):
        for j in range(left, right):
            if L[j] > L[j + 1]:
                swap(L, j + 1, j)
                im = plt.scatter(L, list(range(0, len(L))), c='r', animated=True)
                plt.ylabel("numer pozycji")
                plt.xlabel("liczba na pozycji")
                plt.title("Sortowanie bubblesort")
                ims.append([im])

    ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True,
                                    repeat_delay=1000)
    # ani.save(filename)

    plt.show()


if __name__ == "__main__":
    size = 50
    listNumbers = RandomListNumbers(size)

    ln1 = listNumbers.rand_numbers()
    ln2 = listNumbers.rand_sorted_numbers()
    ln3 = listNumbers.rand_sorted_numbers_rev()
    ln4 = listNumbers.float_gauss()
    ln5 = listNumbers.rand_duplicate_numbers()

    bubblesort(ln1, 0, size - 1, "sort1.gif")
    bubblesort(ln2, 0, size - 1, "sort2.gif")
    bubblesort(ln3, 0, size - 1, "sort3.gif")
    bubblesort(ln4, 0, size - 1, "sort4.gif")
    bubblesort(ln5, 0, size - 1, "sort5.gif")
