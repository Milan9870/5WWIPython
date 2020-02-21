queue = []
invoer = str(input('Een woord:'))

while invoer != 'STOP':
    if invoer == '?':
        if len(queue) > 0:
            print(queue[0])
            queue.pop(0)
    else:
        queue.append(invoer)
    invoer = str(input('Een woord:'))




