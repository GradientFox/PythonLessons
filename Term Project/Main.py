format = "route ADD 66.22.237.{0} MASK 255.255.255.255 0.0.0.0"
lok = "66.22.237.{0}"

# with open("discord-voice-ips-ru.txt", 'r') as f_read, open("discord-ip-ru.bat", 'w') as f_write:
#     response = [format.format(str(ip)) for ip in range(256)]
#     f_write.write('\n'.join(response))

response = [lok.format(str(x)) for x in range(256)]
print(', '.join(response))