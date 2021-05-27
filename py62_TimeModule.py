import time

# epoch = a date and time from which a compute measures system time

print()

# convert a time expressed in seconds since epoch to a readable string
print(time.ctime(0))
# epoch = when your computer thinks time began (reference point)
print(time.ctime(1600000000))
print()

print(time.time())              # return current seconds since epoch
print(time.ctime(time.time()))  # will get current time
print()

# time.strftime(format, time_object) = formats a time_object to a string
localtime_object = time.localtime()     # local time
UTCtime_object = time.gmtime()          # UTC time
print(localtime_object)
print(UTCtime_object)
# format directive such as %d = Day
local_time = time.strftime("%d %B %Y %H:%M:%S", localtime_object)
UTC_time = time.strftime("%d %B %Y %H:%M:%S", UTCtime_object)
print(local_time)
print(UTC_time)
print()

# time.strptime(string_string, format) = parses a string representing time/date and returns a struct_time object
time_string = "27 May, 2021"
time_object = time.strptime(time_string, "%d %B, %Y")
print(time_object)
print()

# time.asctime(time_tuple) = accepts a time_object or a tuple up to 9 elements and returns a string
# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
time_tuple = (2021, 5, 28, 0, 2, 1, 0, 0, 0)
time_string = time.asctime(time_tuple)
mktime_string = time.mktime(time_tuple)
print(time_string)
print(mktime_string)
print()

print()

print()