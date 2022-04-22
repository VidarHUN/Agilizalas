import re

f = open('logs/WCG100140020.txt', 'r')
log_text = f.read()

f.close()

all_messages = re.split(r"\d{4}\/[a-zA-Z]{3}\/\d{2} \d{2}:\d{2}:\d{2}.\d{6}", log_text)

print(all_messages[0])

sip_messages = []

for item in all_messages:
    if ("PORTEVENT" in item or "TIMEROP" in item) and "internalMessage" in item:
        sip_messages.append(item)

print(len(sip_messages))
print(sip_messages[0])
