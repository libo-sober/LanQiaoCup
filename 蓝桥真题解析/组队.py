class Team:
    def __init__(self, info):
        self.info = info


team = []
ans = 0

with open('../数据/team.txt', mode='r', encoding='utf-8') as f:
    for line in f:
        team.append(Team(list(line.strip().split())))

for i in range(20):
    for j in range(i+1, 20):
        for k in range(j+1, 20):
            for m in range(k+1, 20):
                for n in range(m+1, 20):
                    temp = int(team[i].info[1]) + int(team[j].info[2]) + int(team[k].info[3]) + int(team[m].info[4]) + int(team[n].info[5])
                    if temp > ans:
                        ans = temp

print(ans)
