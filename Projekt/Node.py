class Node:
    """
    Klasa reprezentująca węzeł listy jednokierunkowej.

    ...

    Attributes
    --------
    data : int
        Korzen dla drzewa, jesli podana zostanie liczba zostanie utworzony przy pomocy niej Node

    Methods
    -------
    __str__()
        Zwaraca przechowywana liczbe w formacie string

    is_leaf()
        Sprawdzenie czy dany node przechowuje innego noda

    """

    def __init__(self, data=None):
        """
        Parameters
        ----------
        data : int
            Liczba do przechowania
        """

        self.left = None
        self.right = None
        self.data = data

    def __str__(self):
        """Zwaraca przechowywana liczbe w formacie string

        Returns
        -------
        string
            Liczba w formacie string
        """

        return str(self.data)

    def is_leaf(self):
        """Sprawdza czy node ma jakiegos potomka

        Returns
        -------
        bool
            True jesli nie istnieje, False jesli istnieje
        """

        if self.right is not None or self.left is not None:
            return False
        else:
            return True
