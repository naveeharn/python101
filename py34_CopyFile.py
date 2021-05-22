# copyfile()    copies contents of a file
# copy()        copyfile() + permission mode + destination can be a directory
# copy2()       copy() + copies metadata (file’s creation and modification times)

import shutil

shutil.copyfile('py34_text.txt','py34_copyfileText')
shutil.copyfile('py34_text.txt','/Users/naveeharntehmarn/Desktop/Sophomore/2_semester_1/everythingPython/python101/py34_copyfileText')

# shutil.copy('py34_text.txt','py34_copyfileText')
# shutil.copy2(('py34_text.txt','py34_copyfileText'))