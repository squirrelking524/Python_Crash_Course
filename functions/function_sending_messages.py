def show_messages(text_msgs, sent_msgs):
    while text_msgs:
        text = text_msgs.pop()
        print(f"Your text message says, '{text}'.")
        sent_msgs.append(text)

def show_sent_messages(sent_msgs):
    print("\nThe following text messages have been sent:")
    for sent_msg in sent_msgs:
        print(sent_msg)

text_msgs = ['Hey, r u there?', 'when u comin?', 'whats up bro?']
sent_msgs = []

show_messages(text_msgs, sent_msgs)
show_sent_messages(sent_msgs)