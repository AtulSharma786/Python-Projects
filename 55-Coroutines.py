def searcher():
    import time
    # 4 seconds consuming task
    book = "this is a book of atul sharma"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("yes")
        else:
            print("no")


search = searcher()
next(search)
search.send("atul")
input("press something")
search.send("luta")

search.close()
# search.send("luta")
