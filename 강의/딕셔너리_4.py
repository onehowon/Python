EngDic = {"check":["검사하다", "조사하다"], "assign" : ["할당하다", "배정하다"],"involved":["관계된", "연루된"]}
for item in EngDic.keys():
    print(item, ":")
    for val in EngDic[item]:
        print(val, end="")
    print()