import re

txt = '2014/Oct/24 19:16:44.288792 mtc PORTEVENT WCG10014_0624.ttcn:34(testcase:WCG100140624) Port dnsInternalPort[1] was started.'
pattern = "\d{4}.[a-zA-Z]{3}.\d{2} (\d{2}.){3}\d{6}"
txt2 = "2014/Oct/24 19:16:44.812077 1709 PORTEVENT sipClientInterface.ttcn:78(function:sipRun) Message enqueued on sipInternalPort from mtc @variables.internalPortMessageWithAspsSip : {"
out = re.split(pattern, txt2)
print(out)

a="                            body := {"
b = "        parameters := {"

# Hány space van az elején
print(len(a) - len(a.lstrip()))
print(len(b) - len(b.lstrip()))

print('-------------------------------')
f = open('logs\WCG100140020.txt', "r")
lista = []
for x in f:
    stripped = x.lstrip()
    param_depth = int((len(x) - len(x.lstrip()))/4)
    key = stripped.split(" ")[0]
    # Ha az első szó betű vagy szám
    if key.isalnum():
        lista.append((key,param_depth))

print(lista)

