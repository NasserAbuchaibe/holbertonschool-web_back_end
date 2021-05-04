#!/usr/bin/python3
"""sumary_line"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """[summary]

    Args:
        BaseCaching ([type]): [description]
    """

    def put(self, key, item):
        """[summary]

        Args:
            key ([type]): [description]
            item ([type]): [description]
        """
        if key and item:
            self.cache_data[key] = item

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
