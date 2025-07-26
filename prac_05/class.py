def strings_to_length_dict(strings):

    result = {}
    for s in strings:
        result[s] = len(s)
    return result

# 示例用法
if __name__ == "__main__":
    words = ["apple", "banana", "cherry", "kiwi"]
    length_dict = strings_to_length_dict(words)
    print("String versus length：")
    print(length_dict)
