def show_messages(texts):
    for text in texts:
        msg = f"Your text message is: {text}"
        print(msg)

text_msgs = ['Hey, r u there?', 'when u comin?', 'whats up bro?']
show_messages(text_msgs)