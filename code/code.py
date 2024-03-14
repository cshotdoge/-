import random
import pandas as pd

def Bothree(t1, t2):
    score = [0, 0]
    seq = [i * 0.0333 for i in range(16)]
    th = 0.5 + seq[t1] - seq[t2]
    daman = 0
    while score[0] < 2 and score[1] < 2:
        coin = random.random()
        if coin < th:
            score[0] += 1
        if coin >= th:
            score[1] += 1
    if score[0] + score[1] == 3:
        daman = 1
    if score[0] == 2:
        return [t1, t2,daman]
    if score[1] == 2:
        return [t2, t1,daman]

def Boseven(t1, t2):
    score = [0, 0]
    seq = [i * 0.0333 for i in range(16)]
    th = 0.5 + seq[t1] - seq[t2]
    while score[0] < 4 and score[1] < 4:
        coin = random.random()
        if coin < th:
            score[0] += 1
        if coin >= th:
            score[1] += 1
    if score[0] == 4:
        return [t1, t2]
    if score[1] == 4:
        return [t2, t1]

def Ingroup(wkk, i, j):
    daman = 0
    random.shuffle(wkk[i][j])
    for k in range(int(len(wkk[i][j]) / 2)):
        res = Bothree(wkk[i][j][2 * k], wkk[i][j][2 * k+1])
        wkk[i + 1][j].append(res[0])
        wkk[i][j + 1].append(res[1])
        if res[2] == 1:
            daman += 1
    return [wkk,daman]

def Swiss():
    f_list = []
    wkk = [[], [], [], []]
    for i in range(4):
        wkk[i].append([])
        wkk[i].append([])
        wkk[i].append([])
        wkk[i].append([])

    dic = {}
    wkk[0][0] = [i for i in range(16)]
    for i in wkk[0][0]:
        dic[i] = 0
    daman = 0
    list = [[0,0],[1,0],[0,1],[2,0],[0,2],[1,1],[2,1],[1,2],[2,2]]
    for l in list:
        re = Ingroup(wkk, l[0], l[1])
        wkk = re[0]
        daman += re[1]



    rate = daman/33
    f_list = wkk[3][0] + wkk[3][1] + wkk[3][2]
    return [f_list,rate]

def dxh():
    dicc = {}
    daman = 0
    for i in range(16):
        dicc[i] = 0
    for i in range(1, 16):
        for j in range(i):
            res = Bothree(j, i)
            dicc[res[0]] += 1
            daman += res[2]
    rate = daman/120
    ranking = sorted(dicc.items(), key=lambda x: x[1], reverse=True)
    f_list = [item[0] for item in ranking][0:8]
    return [f_list,rate]

def tts(lst):
    random.shuffle(lst)
    baqiang = []
    jinsi = []
    siqiang = []
    juesai = []
    for i in range(4):
        res0 = Boseven(lst[2*i],lst[2*i+1])
        baqiang.append(res0[1])
        jinsi.append(res0[0])
    for j in range(2):
        res1 = Boseven(jinsi[2*j],jinsi[2*j+1])
        siqiang.append(res1[1])
        juesai.append(res1[0])
    guanjun = []
    yajun = []
    res2 = Boseven(juesai[0], juesai[1])
    return [baqiang,siqiang,[res2[1]],[res2[0]]]

def shiguan():
    lst1 = [15,14,13,12,11,10,9,8]
    lst2 = [1,2,3,4,5,6,7,0]
    random.shuffle(lst1)
    random.shuffle(lst2)
    zu = [[],[],[],[]]
    for i in range(4):
        zu[i].append(lst1[2*i])
        zu[i].append(lst1[2*i+1])
        zu[i].append(lst2[2*i])
        zu[i].append(lst2[2*i+1])
    fl = [{},{},{},{}]
    daman = 0
    fg_list = []
    for i in range(4):
        for j in range(4):
            fl[i][zu[i][j]] = 0
    for i in range(4):
        for j in range(3):
            for k in range(j+1):
                jb = Bothree(zu[i][k],zu[i][j+1])
                win = jb[0]
                fl[i][win] += 1
                daman = daman + jb[2]
        ranking = sorted(fl[i].items(), key=lambda x: x[1], reverse=True)
        f_list = [item[0] for item in ranking][0:2]
        fg_list = fg_list + f_list
    rate = daman/24
    return [fg_list,rate]

def ttq(list):
    lst = [list[0],list[7],list[3],list[4],list[1],list[6],list[2],list[5]]
    baqiang = []
    jinsi = []
    siqiang = []
    juesai = []
    for i in range(4):
        res0 = Boseven(lst[2*i],lst[2*i+1])
        baqiang.append(res0[1])
        jinsi.append(res0[0])
    for j in range(2):
        res1 = Boseven(jinsi[2*j],jinsi[2*j+1])
        siqiang.append(res1[1])
        juesai.append(res1[0])
    guanjun = []
    yajun = []
    res2 = Boseven(juesai[0], juesai[1])
    return [baqiang,siqiang,[res2[1]],[res2[0]]]

def ttp(list):
    qiang = []
    ruo = []
    for i in range(4):
        qiang.append(list[2*i])
        ruo.append((list[2*i+1]))
    random.shuffle(qiang)
    random.shuffle(ruo)
    lst = []
    for i in range(4):
        lst.append(qiang[i])
        lst.append((ruo[i]))
    baqiang = []
    jinsi = []
    siqiang = []
    juesai = []
    for i in range(4):
        res0 = Boseven(lst[2 * i], lst[2 * i + 1])
        baqiang.append(res0[1])
        jinsi.append(res0[0])
    for j in range(2):
        res1 = Boseven(jinsi[2 * j], jinsi[2 * j + 1])
        siqiang.append(res1[1])
        juesai.append(res1[0])
    guanjun = []
    yajun = []
    res2 = Boseven(juesai[0], juesai[1])
    return [baqiang, siqiang, [res2[1]], [res2[0]]]





num_tests = input("运行次数: ")
f_dic = {}
for i in range(16):
    f_dic[i] = 0
n = 0
duke = {}
print("瑞士轮")
Sw_rate = 0
for i in range(16):
    duke[i] = [0,0,0,0]
while n < int(num_tests):
    n = n + 1
    f_list = Swiss()[0]
    Sw_rate += Swiss()[1]
    for team in f_list:
        f_dic[team] += 1
    rrr = tts(f_list)
    for i in range(4):
        for j in range(len(rrr[i])):
            duke[rrr[i][j]][i] += 1

'''for res in f_dic.items():
    print("第" + str(res[0]+1) + "队晋级的概率：" + str(res[1] / int(num_tests)))'''
print("打满1：" + str(Sw_rate/int(num_tests)))

print("bo3单循环")
ff_dic = {}
for i in range(16):
    ff_dic[i] = 0
m = 0
Bo_rate = 0
dku = {}
for i in range(16):
    dku[i] = [0,0,0,0]
while m < int(num_tests):
    m = m + 1  # Fix this line
    ppp = dxh()
    ff_list = ppp[0]
    Bo_rate += ppp[1]
    for team in ff_list:
        ff_dic[team] += 1
    rrr = tts(ff_list)
    for i in range(4):
        for j in range(len(rrr[i])):
            dku[rrr[i][j]] [i] += 1

print("打满：" + str(Bo_rate / int(num_tests)))

'''for res in ff_dic.items():
    print("第" + str(res[0] + 1) + "队晋级的概率：" + str(res[1] / int(num_tests)))'''



print("bo3定式")
fff_dic = {}

for i in range(16):
    fff_dic[i] = 0
m = 0
dk = {}
Pw_rate = 0
for i in range(16):
    dk[i] = [0,0,0,0]
while m < int(num_tests):
    m = m + 1  # Fix this line
    ppp = dxh()
    fff_list = ppp[0]
    Pw_rate += ppp[1]
    for team in fff_list:
        fff_dic[team] += 1
    rrr = ttq(fff_list)
    for i in range(4):
        for j in range(len(rrr[i])):
            dk[rrr[i][j]] [i] += 1

print("打满：" + str(Pw_rate/ int(num_tests)))

print('试管')
m = 0
SG_rate = 0
dkk = {}
SG_rate = 0
for i in range(16):
    dkk[i] = [0,0,0,0]
while m < int(num_tests):
    m = m + 1  # Fix this line
    res = shiguan()
    fff_list = res[0]
    SG_rate += res[1]
    for team in fff_list:
        fff_dic[team] += 1
    rrr = ttp(fff_list)
    for i in range(4):
        for j in range(len(rrr[i])):
            dkk[rrr[i][j]][i] += 1
print("打满：" + str(SG_rate/ int(num_tests)))


# Create a list of team labels for the table
team_labels = [f"Team {i+1}" for i in range(16)]

# Create a DataFrame to store the probabilities
data = {
    "Team": team_labels,
    "Sw 8": [duke[i][0] / int(num_tests) for i in range(16)],
    "Sw 4": [duke[i][1] / int(num_tests) for i in range(16)],
    "Sw 2": [duke[i][2] / int(num_tests) for i in range(16)],
    "Sw Championship": [duke[i][3] / int(num_tests) for i in range(16)],
    "Bo 8": [dku[i][0] / int(num_tests) for i in range(16)],
    "Bo 4": [dku[i][1] / int(num_tests) for i in range(16)],
    "Bo 2": [dku[i][2] / int(num_tests) for i in range(16)],
    "Bo Championship": [dku[i][3] / int(num_tests) for i in range(16)],
    "PW 8": [dk[i][0] / int(num_tests) for i in range(16)],
    "PW 4": [dk[i][1] / int(num_tests) for i in range(16)],
    "PW 2": [dk[i][2] / int(num_tests) for i in range(16)],
    "PW Championship": [dk[i][3] / int(num_tests) for i in range(16)],
    "SG 8": [dkk[i][0] / int(num_tests) for i in range(16)],
    "SG 4": [dkk[i][1] / int(num_tests) for i in range(16)],
    "SG 2": [dkk[i][2] / int(num_tests) for i in range(16)],
    "SG Championship": [dkk[i][3] / int(num_tests) for i in range(16)]

}


df = pd.DataFrame(data)

# Export the DataFrame to an Excel file
excel_file = "final15.0.xlsx"
df.to_excel(excel_file, index=False)
print(f"Dat has been exported to {excel_file}")
