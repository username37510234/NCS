subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

print(subway.index("조세호"))

subway.append("하하")
print(subway)

subway.insert(1, "정형돈")
print(subway)

print(subway.pop())
print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

num_list = [5, 2, 1, 3, 4]
num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)

num_list.clear()
print(num_list)

mix_list = ["조세호",20,True]
print(mix_list)

num_list.extend(mix_list)
print(num_list)