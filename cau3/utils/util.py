def house(list_name: list, name: str):
    if name in list_name:
        return "ten {} thoa man dieu kien duoc vao nha". format(name)
    #     return True
    # return False


def require(func, list_name: list, name: str) -> bool:
    result = func(list_name, name)
    if result:
        return True
    return False
    # return (result)

# print(house(["aaa", "bbb", "ccc"], "ccc"))
# print(require(house, ["aaa", "bbb", "ccc"], "ccc"))
