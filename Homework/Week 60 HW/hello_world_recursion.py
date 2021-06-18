def hello_world_recursion(times: int) -> str:
    if times <= 0:
        return ''
    print("Hello World ", str(times))
    hello_world_recursion(times-1)


if __name__ == '__main__':
    hello_world_recursion(10)
