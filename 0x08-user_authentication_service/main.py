#!/usr/bin/env python3
""" Test module """


import requests


def register_user(email: str, password: str) -> None:
    """[summary]

    Args:
        email (str): [description]
        password (str): [description]
    """
    r = requests.post('http://127.0.0.1:5000/users', data={
        'email': email,
        'password': password
    })
    assert r.status_code == 200
    assert r.json() == {'email': email, 'message': "user created"}


def log_in_wrong_password(email: str, password: str) -> None:
    """[summary]

    Args:
        email (str): [description]
        password (str): [description]
    """
    r = requests.post('http://127.0.0.1:5000/sessions', data={
        'email': email,
        'password': password
    })
    assert r.status_code == 401


def log_in(email: str, password: str) -> str:
    """[summary]

    Args:
        email (str): [description]
        password (str): [description]

    Returns:
        str: [description]
    """
    r = requests.post('http://127.0.0.1:5000/sessions', data={
        'email': email,
        'password': password
    })
    assert r.status_code == 200
    assert r.json() == {'email': email, 'message': "logged in"}
    # parse the response cookie to return the session_id for other methods
    return r.cookies.get('session_id')


def profile_unlogged() -> None:
    """[summary]
    """
    r = requests.get('http://127.0.0.1:5000/profile')
    assert r.status_code == 403


def profile_logged(session_id: str) -> None:
    """[summary]

    Args:
        session_id (str): [description]
    """
    r = requests.get('http://127.0.0.1:5000/profile', cookies={
        'session_id': session_id
    })
    assert r.status_code == 200
    assert r.json() == {'email': "guillaume@holberton.io"}


def log_out(session_id: str) -> None:
    """[summary]

    Args:
        session_id (str): [description]
    """
    r = requests.delete('http://127.0.0.1:5000/sessions', cookies={
        'session_id': session_id
    })
    # look inside response's history to check that a 302 redirect occured
    for past_r in r.history:
        assert past_r.status_code == 302


def reset_password_token(email: str) -> str:
    """[summary]

    Args:
        email (str): [description]

    Returns:
        str: [description]
    """
    r = requests.post('http://127.0.0.1:5000/reset_password', data={
        'email': email,
    })
    assert r.status_code == 200
    # parse json response to return the reset_token for other methods
    return r.json().get('reset_token')


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """[summary]

    Args:
        email (str): [description]
        reset_token (str): [description]
        new_password (str): [description]
    """
    r = requests.put('http://127.0.0.1:5000/reset_password', data={
        'email': email,
        'reset_token': reset_token,
        'new_password': new_password
    })
    assert r.status_code == 200
    assert r.json() == {'email': email, 'message': "Password updated"}


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
