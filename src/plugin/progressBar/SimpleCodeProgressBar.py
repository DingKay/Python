import sys
import time

print("#### START ####")
for i in range(101):
    sys.stdout.write('\r')
    sys.stdout.write("[%s>%s] %0.2f" % ('-'*i, ' '*(100-i), float(i)/float(100)))
    time.sleep(0.1)
print("")
print("#### END ####")
