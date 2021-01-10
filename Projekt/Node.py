class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

    def __str__(self):
        return str(self.data)

    def is_leaf(self):
        if self.right is not None or self.left is not None:
            return False
        else:
            return True