import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요.")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())

for i in range(1,51):
    with open(str(i)+"주차.txt","w",encoding="utf8") as bogo:
        bogo.write("- {0:02} 주차 주간보고 - : \n".format(i))
        bogo.write("부서 : \n")
        bogo.write("이름 : \n")
        bogo.write("업무 요약 : \n")