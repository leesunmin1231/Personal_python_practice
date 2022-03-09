# 매주 1회 주간 보고
# -x 주차 주간 보고-
# 부서:
# 이름:
# 업무 요약:
# 50주차 까지
# 파일명: 1주차.txt

for i in range(50):
    with open("./quiz7_file/{}주차.txt".format(i+1),"w",encoding="utf8") as report_file:
        report="-{} 주차 주간보고-\n부서 : Frontend\n이름 : 이선민\n업무 요약 : framework 개발".format(i+1)
        report_file.write(report)

# with open("report.txt","r",encoding="utf8") as report_file:
#     print(report_file.read())