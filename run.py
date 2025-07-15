import os,sys,platform
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('chmod +x vipin')
    os.system('./vipin')
elif bit == '32bit':
    os.system('chmod +x vipin32')
    os.system('./vipin32')
else:
    print('device not supported')
