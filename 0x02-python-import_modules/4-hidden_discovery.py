#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    dir_print = dir(hidden_4)
    dir_no_print = '__'
    for i in range(0, len(dir_print)):
        if dir_no_print not in dir_print[i]:
            print(dir_print[i])
