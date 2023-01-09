def get_longest_word(s: str) -> str:
    ans = []
    length = 0
    for item in s.replace("\n", " ").replace("\t", " ").split(" "):
        if len(item) > length:
            ans.append(item)
            length = len(item)

    return ans[-1]
