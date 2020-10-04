def words_to_num():
    """word numbers to numbers"""
    words = ["Ten", "Twenty", "Thirty", "Fourty", "Fifty", "Sixty"]
    numbers = [10, 20, 30, 40, 50, 60]
    final_output = dict(zip(words, numbers))
    print(f"\nFinal_output: {final_output}")


words_to_num()