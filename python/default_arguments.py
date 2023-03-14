#My Code Snippet Only
def print_from_stream(n, stream=EvenStream()):
    for _ in range(n):
        print(stream.get_next())
    stream.__init__()
