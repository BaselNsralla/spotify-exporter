import time
from threading import Thread

def run_every(seconds):
    """ DECORATOR """
    def decorated(original_func):
        """A function needs to be returned so this function doesn't get called on program run"""
        def periodic(owner):
            while(True):
                time.sleep(seconds)
                original_func(owner)
        def self_passer(owner):
            th = Thread(target=periodic, args=(owner,))
            th.setDaemon(True)
            th.start()
        return self_passer       
    return decorated


def paginated_request(url, start, step):
    def next_page():
        _start = start
        while(True):
            yield url.format(_start, step)
            _start += step
    return next_page



def flat_accumulate(original_func):
    """ DECORATOR """
    def decorated(*args, **kwargs):
        results = []
        while True:
            data, has_next = original_func(*args, **kwargs)
            if not has_next:
                break
            resutls = [*results, *data]
        return resutls
    return decorated