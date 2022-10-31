from random import randrange


students = [1, 2, 3, 4, 5]
print(students)
students = [i+100 for i in students]
print(students)

students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)

no = 0
for i in range(1, 51):
    time = randrange(5, 51)
    if time >= 5 and time <= 15:
        no += 1
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

print("총 탑승 승객 : %d 명" % no)
