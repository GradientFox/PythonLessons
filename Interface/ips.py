ip1 = '66.22.216.'
ip2 = '66.22.217.'
resp = ''

def create_ip(t) -> list:
    temp = []
    for i in range(256):
        temp.append(t + str(i))
    return temp

t1 = create_ip(ip1)
t2 = create_ip(ip2)
t1.extend(t2)

resp = ', '.join(t1)

with open('discord.txt', 'w') as f:
    f.write(resp)