#!/usr/bin/python3
"""sumary_line"""


from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """sumary_line"""

    def __init__(self):
        super().__init__()
        self.order_dict = OrderedDict()

    def put(self, key, item):
        """[summary]

        Args:
            key ([type]): [description]
            item ([type]): [description]
        """
        if key and item:
            self.order_dict[key] = item
            self.order_dict.move_to_end(key)
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard = next(iter(self.order_dict))
            del self.cache_data[discard]
            print("DISCARD:", discard)

        if len(self.order_dict) > BaseCaching.MAX_ITEMS:
            self.order_dict.popitem(last=False)

    def get(self, key):
        """[summary]

        Args:
            key ([type]): [description]

        Returns:
            [type]: [description]
        """
        if key in self.cache_data:
            self.order_dict.move_to_end(key)
            return self.cache_data[key]
        return None
