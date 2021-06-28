import operator
text = open("logfile", "r")
d = dict()
ips = []
i=0
for line in text:
    line = line.strip()
    words= line.split("- -")
    ips=words[0]
    ips=ips.split()
    for word in ips:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1
sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
for key in list(sorted_d.keys()):
    if i<8:
        print(key," ",sorted_d[key])
        i=i+1
        
