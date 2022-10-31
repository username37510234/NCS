import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름": "박명수", "나이": 30, "취미": ["축구", "골프", "코딩"]}

# print(profile)
# pickle.dump(profile, profile_file)
# profile_file.close

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)
print(profile)
profile_file.close()
