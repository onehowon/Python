## 딕셔너리 만들기
d = dict(a = 1, b = 3, c = 5)
type(d)

clr_names = {"apple":"red", "banana" : "yellow"}
print(clr_names)

clr_names["apple"]

clr_names[0] # 인덱싱 지원 x 에러발생

clr_names["cherry"] = "red"
print(clr_names)