import openpyxl

filename= "파일 이름"
sheetname = "시트 이름"
listdata = [[1,2,3],[4,5,6],[7,8,9]]

excel_file = openpyxl.Workbook() # - Workbook() 으로 엑셀 파일 생성

'''
- 엑셀 파일이 생성되면 디폴트 쉬트가 생성되며, 엑셀파일변수.active 로 해당 쉬트를 선택할 수 있음
- 해당 쉬트 이름을 변경하려면 title 변수값을 변경해주면 됨


excel_sheet = excel_file.active
excel_sheet.title = '리포트'
'''
excel_sheet = excel_file.active

if sheetname != '':
    excel_sheet.title = sheetname

for item in listdata:
    excel_sheet.append(item)
'''
- 데이터 추가하기 
  - 가장 간단한 방법으로 엑셀파일변수.append(리스트 형태의 하나의 행 데이터) 를 사용하여, 
  한 줄의 데이터 묶음을 쓸 수 있음
'''
excel_file.save(filename+".xlsx")
excel_file.close()