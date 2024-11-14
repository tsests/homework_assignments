### 4. Секретное сообщение
def main():
    text_data: str = """yesterday, I stArted reading a new book. it's about ancient MythS 
    and hOw They Influence ouR modErn worlD. honestly, i am amazed by the connections and 
    the time the author Put into researching everything. it made me wonder if there are
    mysteries hidden in our everyday LivEs too. Anyway, it waS inspiring, and now i'm morE
    curiouS About history. i just wish i had more time to explore these kinds of things.
    its surprising how much you can learn just by reading stories from different times
    and cultures. sometimes it feels like each myth has its own secret message,
    almost like its waiting for someone to unlock it. theres something comforting 
    about knowing people long ago had the same questions and dreams that we haVE 
    today. i guess thats what MakEs history so fascinating—seeing how everything 
    connects, even if centuries have passed."""
    
    for i in text_data:
        if i.isupper() == True:
            print(i, end = "")
    
    print()


if __name__ == "__main__":
    main()
