#!/usr/bin/python3
"""Funn"""

from curses.ascii import ctrl
import time
from threading import Timer


def memoize(func):
    """Memoization implementation"""
    cache = {}

    def wrapper(*args):
        nonlocal cache
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


@memoize
def fab(n):
    return n if n <= 1 else fab(n - 1) + fab(n - 2)


# Rate Limiting


def rate_limited(max_calls, time_frame):
    last_call = []

    def decorator(func):
        def wrapper(*args, **kwargs):
            nonlocal last_call

            current_time = time.time()
            last_call = [t for t in last_call if current_time - t < time_frame]
            if len(last_call) >= max_calls:
                time_to_wait = time_frame - (current_time - last_call[0])
                print(f"You have to wait {time_to_wait:.1f}s")
                time.sleep(time_to_wait)
            last_call.append(time.time())
            return func(*args, **kwargs)

        return wrapper

    return decorator


@rate_limited(max_calls=2, time_frame=5)
def do_something():
    print("Data Fetched!")


# Debounce
def debounce(delay):
    last_call = 0
    pending = False

    def decorator(func):
        def wrapper(*args, **kwargs):
            nonlocal last_call, pending
            current_time = time.time()

            def execute_later():
                time.sleep(delay)
                nonlocal pending
                if pending:
                    pending = False
                    return func(*args, **kwargs)

            if current_time - last_call < delay:
                print(f"Debounced! for {delay - (current_time - last_call):.2f}")
                pending = True
                execute_later()
            else:
                last_call = current_time
                return func(*args, **kwargs)

        return wrapper

    return decorator


def t_debounce(delay):
    timer = None

    def decorator(func):
        def wrapper(*args, **kwargs):
            nonlocal timer
            if timer:
                timer.cancel()
            timer = Timer(delay, func, args, kwargs)
            timer.start()

        return wrapper

    return decorator


@t_debounce(delay=1.0)
def search(query):
    print(f"Searching For: {query}")

def make_counter():
    ctr = 0

    def increment():
        nonlocal ctr
        ctr += 1
        return ctr
    
    def reset():
        nonlocal ctr
        ctr = 0
    
    return increment, reset


if __name__ == "__main__":
    search("a")
    search("ab")
    search("abc")
    search("abcd")
    search("abcde")
    search("abcdefg")
