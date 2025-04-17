print("Welcome to the Mad Libs Game!")
print("Let's create a funny little story. Please answer the following:\n")

name = input("Enter a name: ")
hobby = input("Enter a hobby: ")
color = input("Enter a color: ")
thing = input("Enter a random object: ")
place = input("Enter a place: ")
adjective = input("Enter an adjective: ")

story = f"""
Once upon a time, there was a person named {name} who loved {hobby}.
One day, they wore a {color} hat and grabbed their favorite {thing}.
Then, they went to {place} to find something {adjective}.
It turned out to be the best day ever!
"""
print("\nHere’s your story:")
print(story)
