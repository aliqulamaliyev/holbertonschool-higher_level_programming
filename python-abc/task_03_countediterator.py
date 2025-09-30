class CountedIterator:
    def __init__(self, iterable):
        # create an iterator from the given iterable
        self._iterator = iter(iterable)
        # start the counter at 0
        self._count = 0

    def __next__(self):
        """Return the next item and increment the counter."""
        # try to get the next item from the underlying iterator
        item = next(self._iterator)  # will raise StopIteration if no more items
        self._count += 1
        return item

    def get_count(self):
        """Return how many items have been iterated over so far."""
        return self._count

    def __iter__(self):
        """Make CountedIterator itself an iterator."""
        return self

