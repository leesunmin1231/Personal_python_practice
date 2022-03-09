import pickle
# 데이터를 파일로 저장
profile_file=open("profile.pickle","wb") 
# w는 write 할때 w, b는 binary 할때 b. pickle을 쓰기 위해서는 항상 binary type을 정의 해줘야 함
profile={"name":"min","age":23}
pickle.dump(profile,profile_file) 
# profile 이라는 딕셔너리에 있는 정보를 profile_file이라는 파일에 저장
profile_file.close()

# profile_file=open("profile.pickle","rb")
# # 피클 파일 읽어오기
# profile=pickle.load(profile_file)
# print(profile)
# profile_file.close()
# # pickle은 애초에 사람이 읽는 파일이 아니다. 즉 불러오기를 통해서만 읽을 수 있다.