#!/usr/bin/env python3
""" Auth """

from flask import request
from typing import List, TypeVar


class Auth:
    """ Authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """[summary]

        Args:
            path (str): [description]
            excluded_paths (List[str]): [description]

        Returns:
            bool: [description]
        """
        return False

    def authorization_header(self, request=None) -> str:
        """[summary]

        Args:
            request ([type], optional): [description]. Defaults to None.

        Returns:
            str: [description]
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """[summary]

        Returns:
            [type]: [description]
        """
        return None
