#!/usr/bin/python
#
# convert ergebnis.txt to html tabelle
#

fd = open("ergebnis.txt", "r")
lines = fd.readlines()
fd.close()

t=[]
a=[]
for line in lines:
    if "boot" in line:
        if len(a)!=0:
            t.append(a)
        a=[]
        s = line.strip().split("boot: ")[1]
        a.append(s)
    if "map" in line:
        s1 = line.strip().split(" ")[3]
        s2 = s1.split(":")[0]
        a.append(s2)

zeilen = len(t)


print "<html><body><table border=\"1\">"
for y in range(61):
    print "<tr><td>",y,"</td>",
    for x in range(zeilen):
        if y==0 :
            print "<td>",t[x][y],"</td>",
        else:
            if int(t[x][y]) != 1:
                print "<td bgcolor=\"#FF0000\">F</td>",
            else:
                print "<td> </td>",
    print "</tr>"
print "</table></body></html>"
