while True:
    try:
        with open('dansfile.txt', 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File not found. Please ensure 'dansfile.txt' exists.")
    except Exception as e:
        print(f"An error occurred: {e}")
    break