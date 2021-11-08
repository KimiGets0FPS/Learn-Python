def final_val_after_op(operations: list[str]) -> int:
    output = 0
    for i in range(len(operations)):
        print(operations[i])
        if operations[i] == "--X" or operations[i] == "X--":
            output -= 1
        else:
            output += 1
    return output


print(final_val_after_op(["X++", "++X", "--X", "X--"]))
