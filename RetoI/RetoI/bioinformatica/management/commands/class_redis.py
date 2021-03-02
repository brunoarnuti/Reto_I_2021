from redis import Redis
from django.core.cache import cache

conn = Redis()

import redis_lock, socket

host_id = "owned-by-%s" % socket.gethostname()
lock = redis_lock.Lock(conn, "name-of-the-lock", id=host_id)
if lock.acquire(blocking=False):
    assert lock.locked() is True
    print("Got the lock.")
    lock.release()
else:
    if lock.get_owner_id() == host_id:
        print("I already acquired this in another process.")
    else:
        print("The lock is held on another machine.")


# def function():
#     val = cache.get(key)
#     if not val:
#         with cache.lock(key):
#             val = cache.get(key)
#             if not val:
#                 # DO EXPENSIVE WORK
#                 val = ...
#                 cache.set(key, value)
#     return val
