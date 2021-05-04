#!/usr/bin/python3
"""sumary_line"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """sumary_line"""

    def __init__(self):
        super().__init__()
        self.indexes = []

    def put(self, key, item):
        """[summary]

        Args:
            key ([type]): [description]
            item ([type]): [description]
        """
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key in self.cache_data:
                    del self.cache_data[key]
                    self.indexes.remove(key)
                else:
                    del self.cache_data[self.indexes[self.MAX_ITEMS - 1]]
                    discard = self.indexes.pop(self.MAX_ITEMS - 1)
                    print("DISCARD:", discard)

            self.cache_data[key] = item
            self.indexes.append(key)

    def get(self, key):
        """[summary]

        Args:
            key ([type]): [description]

        Returns:
            [type]: [description]
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
