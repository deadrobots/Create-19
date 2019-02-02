import multiprocessing
from wallaby import *

def die_after_time(function, time, post_function=None):
    p = multiprocessing.Process(target=function)
    p.start()
    # multiprocessing.Process(target=stop_button, args=(p,)).start()
    p.join(time)

    if p.is_alive():
        print('The {} seconds are up - ending process'.format(time))
        p.terminate()
        if post_function:
            print('Running post function...')
            post_function()


def stop_button(process):
    while not left_button():
        pass
    process.terminate()
    print('KILLED')
