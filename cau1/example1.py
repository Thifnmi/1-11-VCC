class person:

    def __init__(self, name):
        self.name = name

    def print_name(self):
        print("tên của bạn là {}". format(self.name))


ob = person("thìn")
ob.print_name()

# run with script: python script.py
# run with load module:  python -m module
