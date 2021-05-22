
try:
    with open("py32_text.stxt") as file:
        print(file.read())
        print(file.closed)
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)

