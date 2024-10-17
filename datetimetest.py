from datetime import datetime

from os.path import join as pjoin



date = datetime.now()
date_time = date.strftime("%m/%d/%Y_%H:%M:%S") + '.txt'
print(date_time)

path_to_file = pjoin('C:\\', 'Desktop', date_time)

savefile = open(path_to_file, "w")

for i in range(10):
    savefile.write("This is line %d\r\n" % (i+1))

savefile.close()