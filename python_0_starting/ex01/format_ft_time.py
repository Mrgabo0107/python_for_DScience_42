import time

# time from epoch
pureTime = time.time()

# set a struct time where there are all the date values calculated
local = time.localtime()

# print pureTime in two formats
print(f"Seconds since January 1, 1970: {pureTime:,.4f} or "
      f"{pureTime:.2e} in scientific notation")

# print localtime in the asked format
print(time.strftime("%h %d %Y", local))
