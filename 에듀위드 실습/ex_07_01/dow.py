han = open("mbox-short.txt")
for line in han:
    line = line.rstrip()
    #print(line) - 오류 확인하기 위해...시험삼아
    wds = line.split()
    #print(wds)
    # guardian
    # 1. if len(wds) < 3:
        #continue
    # 2. or 순서중요!! 가디언패턴이 앞에
    # or은 앞문장이 참이면 뒤에는 확인안함
    if len(wds) < 3 or wds[0] != 'From':
        #print("ignore")
        continue
    print(wds[2])
