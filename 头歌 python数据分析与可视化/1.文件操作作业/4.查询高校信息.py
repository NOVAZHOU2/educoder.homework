def readfile1(filename):  # 用于筛选出概率大于等于80%，返回列表
    ls = []
    with open('step5/admit2.csv', "r") as fp:
        s = fp.readline()
        s = fp.readline()
        while s:
            l = s.strip().split(",")
            if eval(l[-1]) >= 0.8:
                ls.append(l)
            s = fp.readline()
    return ls


def readfile2(filename):  # 用于筛选出概率大于等于90%以及小于等于70%,返回列表
    ls1 = []
    ls2 = []
    with open('step5/admit2.csv', "r") as fp:
        s = fp.readline()
        s = fp.readline()
        while s:
            l = s.strip().split(",")
            if eval(l[-1]) >= 0.9:
                ls1.append(l)
            if eval(l[-1]) <= 0.7:
                ls2.append(l)
            s = fp.readline()
    return ls1, ls2


n = input()
if n == '1':
    ls = readfile1("step5/admit2.csv")
    cnt = 0  # 用于记录排名大于4的个数
    for row in ls:
        if eval(row[1]) >= 4:
            cnt += 1
    print("Top University in >=80%%:%.2f%%" % (cnt / len(ls) * 100))
elif n == 'Research':
    ls1, ls2 = readfile2("step5/admit2.csv")
    # print(ls1)
    cnt1 = len([i for i in ls1 if i[-4] == '1'])  # 大于90%，且有研究经历的个数
    cnt2 = len([i for i in ls2 if i[-4] == '1'])  # 小于70%，且有研究经历的个数
    print("Research in >=90%%:%.2f%%" % (cnt1 / len(ls1) * 100))
    print("Research in <=70%%:%.2f%%" % (cnt2 / len(ls2) * 100))
elif n == '2':
    ls = readfile1("admit2.csv")
    l = []  # 保存所有TOEFL分数
    for i in ls:
        l.append(float(i[3]))
    print("TOEFL Average Score:%.2f" % (sum(l) / len(l)))
    print("TOEFL Max Score:%.2f" % max(l))
    print("TOEFL Min Score:%.2f" % min(l))
elif n == '3':
    ls = readfile1("step5/admit2.csv")
    l = []  # 保存所有绩点分数
    for i in ls:
        l.append(float(i[-5]))
    print("CGPA Average Score:%.3f" % (sum(l) / len(l)))
    print("CGPA Max Score:%.3f" % max(l))
    print("CGPA Min Score:%.3f" % min(l))
else:
    print("ERROR")