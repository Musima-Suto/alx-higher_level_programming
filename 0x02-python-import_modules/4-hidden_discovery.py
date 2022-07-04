#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    nm_definitions = dir(hidden_4)
    for i in nm_definitions:
        if i[:2] != "__":
            print(i)
