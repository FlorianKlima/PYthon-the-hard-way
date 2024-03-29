def print_keyword_args(**kwargs):

    print("\n")
    print(kwargs)
    print(type(kwargs))

    for key, value in kwargs.items():
        print(f"{key} = {value}")

    third = kwargs.get("third")
    if third != None:
        print("third arg =", third)


print_keyword_args(first="a")
print_keyword_args(first="b", second="c")
print_keyword_args(first="d", second="e", third="f")
