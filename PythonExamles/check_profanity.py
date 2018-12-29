def read_text():
    quotes = open("E:/1MAC/FullStack_S/PythonExamles/detect_profanity.txt")
    content_files = quotes.read()
    print(content_files)
    quotes.close()
read_text()
