def fib(n):
    a, b = 0, 1
    count = 1
    while count < n:
        a, b = b, a+b
        count = count + 1
        print(b)
# fib(7)


def compute(*numbers):
    s = 1
    for n in numbers:
        s = s * n + n
    return s


nums = (3, 3)
# print(compute(*nums))
line = [1, 2, 3]
line[len(line):] = [4]
print(line)

with open("a.txt", "r+") as file:
    file.write("abc")

text = "abc123"
for i in text:
    print(i)

dic = {"a", "b"}
dic.update("c")
print(dic)
dic.discard()


def ask(prompt, hint="yes or no", chance=2):
    while chance > 0:
        answer = input(prompt)
        if answer.lower() in ('y', 'yes'):
            print("Thank you")
            return True
        if answer.lower() in ('n', 'no'):
            print("Why not")
            return False
        else:
            chance -= 1
            print("yes or no")
    print("Sorry, you have tried too many times.")
# ask("Do you like SciPy?")


fp = open('test.txt', 'r+', 0)
fp.readline()
fp.seek(10, 1)
print(fp.readline())
