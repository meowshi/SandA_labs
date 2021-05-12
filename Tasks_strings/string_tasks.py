def task1(string1, string2):
    if (len(string1) != len(string2)):
        print("Разная длина")
        return False
    max_string1 = str()
    max_string2 = str()
    for _ in range(len(string1)):
        max_string1 += max(string1)
        max_string2 += max(string2)
        string1 = string1.replace(max(string1), "", 1)
        string2 = string2.replace(max(string2), "", 1)
    for i in range(len(max_string1)):
        if max_string1[i] < max_string2[i]:
            for j in range(len(max_string2)):
                if max_string1[j] > max_string2[j]: return False
    return True


def is_palindrome(string):
    string_len = len(string)
    for i in range (string_len // 2):
        if string[i] != string[string_len - 1 - i]: return False
    return True

def task2(string):
    for i in range(len(string), 0, -1):
        for j in range(len(string) - i + 1):
            if (is_palindrome(string[j:i + j])): return string[j:i + j]

def task3(string):
    # список учтенных подстрок
    substrings = list()
    string_len = len(string)
    for i in range(string_len // 2):
        for j in range(string_len - i):
            substring = string[j:j + i + 1] + string[j:j + i + 1]
            if string.find(substring) != -1:
                if substring not in substrings:
                    substrings.append(substring)
    return len(substrings)