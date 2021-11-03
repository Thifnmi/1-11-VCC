# OOP python
# đóng gói: che giấu thông tin
# kế thừa: xây dựng lớp mới từ lớp có sẵn, lớp mới sẽ bao gồm các thuộc tính
# của lớp có sẵn và các thuộc tính mới của nó
# đa hình: 1 phương thức có thể thực hiện theo nhiều cách khác nhau
# trừu trượng: tổng quát hóa phương thức mà không quan tâm đến phương thức
# thực hiện ra sao(có tên phương thức nhưng không có body)

# đa kế thừa: 1 lớp có nhiều cha được gọi là đa kế thừa, lớp con sẽ ưu tiên kế
# thừa các phương thức, thuộc tính của lớp cha đầu tiên trong danh sách kế thừa
# kế thừa đa cấp: lớp b kế thừa lớp a và lớp c kế thừa lại lớp b thì được gọi
# là kế thừa đa cấp

# contructor(hàm tạo)
# __new__ là bước đầu tiên trong quá trình khởi tạo,nó được gọi đến đâu tiên
# để khỏi tạo đối tượng và luôn luôn trả về giá trị, nhận đối số là lớp(cls)
# __init__ không trả về giá trị, chỉ chịu trách nhiệm khỏi tạo phiên bản sau
# khi nó được tạo, nhận đối số là chính nó(self) giống như this trong java


import random


class Bankaccount:
    def __init__(self, balance: int):
        self.balance = balance

    def deposit(self, dp: int):
        self.dp = dp
        print(f"new balance affter deposit: {self.balance + self.dp}")

    def withdraw(self, wd: int):
        self.wd = wd
        print("new balance affter withdraw: {}".format(
            int(self.balance - (self.wd + (self.wd / 100 * 5)))))


class VPBank(Bankaccount):
    def deposit(self, dp: int):
        return super().deposit(dp)

    def withdraw(self, wd: int):
        return super().withdraw(wd)
    # def deposit(self, dp: int):
    #     self.dp = dp
    #     print(f"new balance affter deposit: {self.balance + self.dp}")

    # def withdraw(self, wd):
    #     self.wd = wd
    #     print("new balance affter withdraw: {}".format(
    #         int(self.balance - (self.wd + (self.wd / 100 * 5)))))


class TechcomBank(Bankaccount):
    def deposit(self, dp: int):
        return super().deposit(dp)

    def withdraw(self, wd: int):
        return super().withdraw(wd)
    # def deposit(self, dp: int):
    #     self.dp = dp
    #     print(f"new balance affter deposit: {self.balance + self.dp}")

    # def withdraw(self, wd):
    #     self.wd = wd
    #     print("new balance affter withdraw: {}".format(
    #         int(self.balance - (self.wd + (self.wd / 100 * 5)))))


list_bank_account = [VPBank(50000000), TechcomBank(90000000), TechcomBank(
    8000000), TechcomBank(5000000000), VPBank(6000000000)]


def random_dp_wd():
    result = random.randint(0, 1)
    return result


for account in list_bank_account:
    result = random_dp_wd()
    if(result == 1):
        account.deposit(10000)
    else:
        account.withdraw(100000)
