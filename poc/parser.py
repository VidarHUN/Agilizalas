import re

 # barna regex kódja
f = open('logs\WCG100140020.txt', 'r')
log_text = f.read()

f.close()

all_messages = re.split("\d{4}\/[a-zA-Z]{3}\/\d{2} \d{2}:\d{2}:\d{2}.\d{6}", log_text)

print(all_messages[0])

sip_messages = []

for item in all_messages:
    if ("PORTEVENT" in item or "TIMEROP" in item) and "internalMessage" in item:
        sip_messages.append(item)

print(len(sip_messages))
print(sip_messages[0])

# nem minden mezőt szed ki a regex

# timestamp = sip_messages[0].split()[0]
sending_component = sip_messages[0].split()[0]
print("sending_component: ", sending_component)
event_type = sip_messages[0].split()[1]
print("event_type: ", event_type)
operation_type = sip_messages[0].split()[3]
print("operation_type: ", operation_type)
receiving_component = sip_messages[0].split()[7]
print("receiving_component: ", receiving_component)

originator = sip_messages[0].split()[2]
operation = sip_messages[0].split()[3]

# message = sip_messages[0].split()[6]
# keys = sip_messages[0].split()[7]


# internal message kulcsokat szedi ki és a mélységüket. Most még csak az első üzeneten
list = []
for x in sip_messages[0].splitlines():
    stripped = x.lstrip()
    param_depth = int((len(x) - len(x.lstrip()))/4)
    key = stripped.split(" ")[0]
    # Ha az első szó betű vagy szám
    if key.isalnum():
        list.append((key,param_depth))

mykey = []
print("-------------------------")
print(list)
print("-------------------------")

# kulcs- mélység párosból "csinálna" egymásba ágyazott listát.
# Lehet máshogy tárolva egyszerűbb lenne használni.
y = -1
for i in list:
    if(i[1] == 1):
        y += 2
        mykey.append(i[0])
        mykey.append([])
    if(i[1] == 2 or i[1] == 3):
        mykey[y].append(i[0])
    #print(mykey)
        

# mykey = lista[1][0]
print(mykey)
print(list)