class Stack:
    """A custom datatype with both LIFO and FIFO support.

    Attributes:
        items (:obj:`list`): Items stored in the stack (top of the stack is
            `items[0]`).

    """

    def __init__(self):
        self.items = []


    def push(self, *ms):
        """Pushes items to the top of the stack.

        Args:
            *ms: Items to be pushed.

        """

        for m in ms:
            self.items.insert(0, m)


    def add(self, *ms):
        """Pushes items to the bottom of the stack.

        Args:
            *ms: Items to be pushed.

        """

        self.items.extend(ms)



    def pop(self):
        """Removes the top of the stack.

        Returns:
            The popped item.
        """

        return self.items.pop(0)


    def get(self, i):
        """Retrieves a stack item by index.

        Args:
            i (int): The index.

        Returns:
            The item at the index or `None` if the index is out of
            range.
        """

        if len(self.items) > i:
            return self.items[i]

