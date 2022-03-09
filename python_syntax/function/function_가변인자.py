def profile(name, age,subject1,subject2,subject3):
    print("이름: {}, 나이: {}".format(name,age), end=" ")
    print("배우는 과목: {} {} {}".format(subject1,subject2,subject3))

profile("이선민",24,"물리","화학","지구과학")

def profile_other(name, age,*subject):   # 가변 인자. 입력될 인자가 몇개인지 모를 경우 사용
    print("이름: {}, 나이: {}".format(name,age), end=" ")
    print("배우는 과목:",end=" ")
    for lang in subject:
        print(lang,end=" ")

profile_other("이선민",24, "물리","화학")
profile_other("dltjsals",24,"일반역학","전자기학","열역학","운영체제","자료구조","알고리즘")