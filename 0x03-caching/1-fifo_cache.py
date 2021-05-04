#!/usr/bin/python3
"""sumary_line"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
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
            if key in self.cache_data:
                self.cache_data[key] = item
                return

            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard = self.indexes.pop(0)
                del self.cache_data[discard]
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
