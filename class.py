class Father:
    def __init__(self):
        self.value = 0

    def add(self, num):
        self.value += num
        return self.value

# def add(num):
#     return num

# kim = Father()

# print(kim.add(3))
class Mother:
    def __init__(self):
        self.first = 1
        self.second = 2

    def return_first(self):
        return self.first
    def return_second(self):
        return self.second
    def add(self, num1, num2):
        return self.first+self.second+num1+num2
        
# print(add(5))

lee = Mother()
print(lee.return_first())
print(lee.return_second())
print(lee.add(10, 20))