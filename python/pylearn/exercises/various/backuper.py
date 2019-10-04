import os.path, sys
import ftplib

def report(msg):
  print("[i] {}".format(msg))

server_data = {
 "address": "1.2.3.4:21",
 "login"  : "aaa",
 "pass"   : "aoo",
 "path"   : "path where is files on server"
}

save_path = "some path where is downloaded files will be saved"
os.chdir(save_path)

ftp = ftplib.FTP(server_data["address"])
report("Connected to {}.".format(server_data["address"]))

ftp.login(server_data["login"], server_data["pass"])
report("Logined as {}@***.".format(server_data["login"]))

ftp.cwd(server_data["path"])
report("Moved to {}.".format(server_data["path"]))

report("Starting transmission.")
files = ftp.nlst()
for file in files:
  local_name = os.path.join(save_path, file)
  
  with open(local_name, 'wb') as file_pointer:
    ftp.retrbinary('RETR '+ file_pointer, file_pointer.write)
  
  file_pointer.close()
  
report("Transmission successful.")
ftp.quit()