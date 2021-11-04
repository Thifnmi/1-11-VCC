def require(original_function):
    def check_name(list_name: list, name: str):
        if name in list_name:
            print(f"ten {name} du dieu kien duoc vao nha")
        print(original_function(list_name, name))
    return check_name


@require
def house(list_name: list, name: str) -> bool:
    if name in list_name:
        return True
    return False


# house(["aaa", "bbb", "ccc"], "ccc")
