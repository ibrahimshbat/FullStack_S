import urllib
def read_text():
    quotes = open("E:/1MAC/FullStack_S/PythonExamles/detect_profanity.txt")
    content_files = quotes.read()
    print(content_files)
    quotes.close()
    check_profanity(content_files)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    connection.close()
    if "true" in output:
        print("Yes, there is course word in my text")
    else:
        print("No, there is not course word in my text")

read_text()
