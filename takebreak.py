import time
import webbroswer

totalbreak = 3
count=0
while count < totalbreak:
    time.sleep(10)
    webbroswer.open("https://www.youtube.com/watch?v=W3ZtOzR55bg")
    count+=1
