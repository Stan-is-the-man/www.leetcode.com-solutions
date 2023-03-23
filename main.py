def longest_commonPrefix(strs: list[str]):
    strs = sorted(strs, key=len)

    for x in range(len(strs[0])):
        to_compare = [0][0]
        current = ''
        for z in range(len(strs[0])):
            if strs[x][z] == to_compare:
                current += strs[x][z]


a = longest_commonPrefix(["flower", "flow", "flight"])
print(a)
