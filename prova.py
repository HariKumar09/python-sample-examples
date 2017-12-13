import os
import win32file
import msvcrt

filename = "prova.log"

# get an handle using win32 API, specifyng the SHARED access!
handle = win32file.CreateFile(filename,
                                win32file.GENERIC_READ,
                                win32file.FILE_SHARE_DELETE |
                                win32file.FILE_SHARE_READ |
                                win32file.FILE_SHARE_WRITE,
                                None,
                                win32file.OPEN_EXISTING,
                                0,
                                None)
# detach the handle
detached_handle = handle.Detach()
# get a file descriptor associated to the handle\
file_descriptor = msvcrt.open_osfhandle(
    detached_handle, os.O_RDONLY)
# open the file descriptor
file = open(file_descriptor)

for line in file:
    print(line)
