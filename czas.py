import time
from datetime import datetime

# time.sleep(1)

# print("jeden")
# time.sleep(2)
# print("dwa")
# time.sleep(2)
# print("trzy")

# print(time.gmtime())

#
# print(time.time())
# print(time.strftime("Jesteśmy w %Y roku i w miesiącu %m, w strefie %Z", time.gmtime()))
# print(datetime.now())

odp = int(input("sekundy..."))
czas = time.gmtime()
if odp == czas[5]:
    print("Gratulacje!")
    print(czas[5])
else:
    print("Nie udało Ci się!")
    print(czas[5])