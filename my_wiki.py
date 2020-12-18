import wikipedia
def mywiki(topic):
    info = wikipedia.summary(topic, sentences=2)
    url = wikipedia.page(topic).url
    print(f"Here is the information about {topic}:\n\n{info}"
          f"\n\nRead more about {topic} : \n{url}")

user_inp = input("Which topic's information do you want?:\n")
if __name__ == '__main__':
    mywiki(user_inp)
