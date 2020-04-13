import time

# True für immer
while True:
    # sleep eine Sekunde, damit der Computer nicht crashed
    time.sleep(1)
    print("running", time.time())  # seconds since 1970,1,1,00:00

print("finished")

# endlosschleife
import time
variable = 10

while True variable == 10:
    time.sleep(1)
    print("running", time.time())  # seconds since 1970,1,1,00:00

print("finished")