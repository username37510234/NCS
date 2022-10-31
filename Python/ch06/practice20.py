def profile(name,age,*langauge):
    print("이름 : {0}\t나이 : {1}\t".format(name,age),end=" ")
    for lang in langauge:
        print(lang, end=" ")
    print()

profile("유재석",20,"Python","Java","C","C++","C#","JavaScript")
profile("김태호",25,"Kotlin","Swift")