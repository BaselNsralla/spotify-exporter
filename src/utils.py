import time
from threading import Thread

def run_every(seconds):
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