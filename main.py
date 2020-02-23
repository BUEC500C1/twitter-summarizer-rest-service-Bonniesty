"""
Usage: Entry of queue system
@author: Tianyi Sun
refence: https://docs.python.org/2/library/queue.html
"""
import getUserTweet2Img as twitter_api
import tweetImg2Video as video_api
import queue
import threading
import random


def run_thread(q):
    while(True):
        name = q.get()
        if name is None:
            break
        status = twitter_api.getUserTwAPI(name, "keys")
        if status == "success!":
            video_api.process_img(name)
            video_api.toVideo(name)
        print("Thread Finished!!!")
        q.task_done()


if __name__ == '__main__':
    q= queue.Queue()
    num = 4
    nameList = ["@AnimalPlanet","@cnnbrk" ]
    tList = []
    i=0
    while i<num:
        t = threading.Thread(target = run_thread, args=(q,))
        t.start()
        i+=1

    for name in nameList:
        q.put(name)
    q.join()

    j=0
    while j<num:
        q.put(None)
        j += 1

