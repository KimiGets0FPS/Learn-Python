def hello_world_recursion(times: int):
    if times > 0:
        print("Hello World ", times)
        hello_world_recursion(times-1)


if __name__ == '__main__':
    hello_world_recursion(10)
