

def run_length_encoding(s):
    encoded_string = ""
    prev = ""
    counter = 0
    for i in s:
        if i is not prev:
            if prev is not "":
                encoded_string += prev + str(counter)
            counter = 1
        else:
            counter += 1
        prev = i
    encoded_string += i + str(counter)
    return encoded_string
