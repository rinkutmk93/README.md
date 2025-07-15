import os,sys,platform
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('chmod +x rinku93')
    os.system('./rinku93')
elif bit == '32bit':
    os.system('chmod +x rinku93')
    os.system('./rinku93')
else:
    print('device not supported')
