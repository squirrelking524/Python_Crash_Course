#from 8-3
'''
def make_shirt(size, text):
    print(f"The shirt size is: {size}; and the text displayed: {text}")


make_shirt("Medium", "Lover of All")
make_shirt(size="Large", text="Hater of All")
'''

def make_shirt(size="Large", text="I love Python"):
    print(f"The shirt size is: {size}; and the text displayed: {text}")

make_shirt()
make_shirt(size="Medium")
make_shirt(size="X-Large", text="I love JavaScript")