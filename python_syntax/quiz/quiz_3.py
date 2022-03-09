# 사이트별로 비밀번호 만들기
'''
site=input("사이트를 입력하시오: ")
first_d=site.index(".")
second_d=site.index(".",first_d+1)
middle=site[first_d+1:second_d]
print(site[first_d+1:first_d+4],len(middle),middle.count("e"),"!")
'''

site=input("사이트를 입력하시오: ")
my_str=site.replace("https://www.","")
my_str=my_str[:my_str.index(".")]
print (my_str)
password=my_str[:3]+str(len(my_str))+str(my_str.count("e"))+"!"
print(password)