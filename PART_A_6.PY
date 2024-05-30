def counter(fname):
    num_words = 0
    num_lines = 0
    num_chars = 0
    try:
        with open(fname, 'r') as f:
            for line in f:
                num_lines += 1
                words = line.split()
                num_words += len(words)
                num_chars += len(line)
            print(f"NUMBER OF WORDS IN TEXT FILE: {num_words}")
            print(f"NUMBER OF LINES IN TEXT FILE: {num_lines}")
            print(f"NUMBER OF CHARACTERS IN TEXT FILE: {num_chars}")
    except FileNotFoundError:
        print("File not found")
fname = "/home/shadow269/VS CODE/PYTHON_4THSEM/Readme.md"
counter(fname)