strs = ["flower", "flow", "flight"]

strs.sort()
print(strs)

s = ""
i = 0
length = len(strs)
print(strs[0][i])
print(strs[length - 1][i])
while i < len(strs[0]):
    if strs[0][i] == strs[ length - 1][i]:
        s += strs[0][i]
    else:
        break
    i += 1
print(s)