# Command line Input
import schedule
import sys
import os
import time
import shutil
import hashlib
import zipfile
import datetime
from email.message import EmailMessage
import smtplib
Border ="-"*50
global lobj

def SendMail(sender, app_password, receiver, subject, body, attachments):

    try:
        msg = EmailMessage()

        # Set headers
        msg["From"] = sender
        msg["To"] = receiver
        msg["Subject"] = subject

        # Set body
        msg.set_content(body)

        # Attach files
        for file in attachments:

            if not os.path.exists(file):
                print(f"Attachment not found: {file}")
                continue

            
            f=open(file,"rb")
            file_data = f.read()
            file_name = os.path.basename(file)
            f.close()
            msg.add_attachment(
                file_data,
                maintype="application",
                subtype="octet-stream",
                filename=file_name
            )

        # Connect to Gmail SMTP Server
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, app_password)
            server.send_message(msg)

        print("Mail sent successfully")

    except Exception as e:
        print("Error while sending mail:", e)


def RestoreBackup(zip_file,destination):
    Ret = True
    Ret= os.path.exists(zip_file)
    if(Ret == False):
        print(f"{zip_file} does not exist\n")
        return
    else:
        if not os.path.exists(destination):
            os.makedirs(destination,exist_ok=True)
    robj=zipfile.ZipFile(zip_file,"r")
    robj.extractall(destination)
    print(f"Backup {zip_file} restored to {destination}")
    robj.close()

def update_history(zip_file,filecount):
    size=os.path.getsize(zip_file)
    shobj=open("DataShieldHistory.txt","a")
    shobj.write(f"Date : {datetime.datetime.now()} No. of Files : {filecount} ZipSize : {size}\n")
    shobj.close()

def show_history():
    
    if os.path.exists("DataShieldHistory.txt"): 
        tobj=open("DataShieldHistory.txt","r") 
        print(tobj.read()) 
    else: 
        print("No backup history found.")
    
def Logfilecreation(LogFolder="log"):
    
    if not os.path.exists(LogFolder):
        try:
            os.mkdir(LogFolder)
        except Exception as e:
            print(f"Error creating log folder: {e}")
            return 

    
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    file_path = os.path.join(LogFolder, f"Marvellous_{timestamp}.log")

    try:
        return open(file_path, "w")   
    except Exception as e:
        print(f"Error creating log file: {e}")
        return 

def make_zip(folder):
    timestamp=time.strftime("%Y-%m-%d_%H-%M-%S")
    zip_name=folder+"_"+timestamp + ".zip"

    # open the zip file
    zobj=zipfile.ZipFile(zip_name,'w',zipfile.ZIP_DEFLATED)

    for root,dirs,files in os.walk(folder):
        for file in files:
            full_path = os.path.join(root,file)
            relative = os.path.relpath(full_path,folder)

            zobj.write(full_path,relative)

    zobj.close()
    lobj.write(zip_name)
    return zip_name

def calculate_hash(path):
    hobj= hashlib.md5()
    fobj=open(path,"rb")
    lobj.write(f"{path} File open to create checksum\n")
    while True:
        Data=fobj.read(1024)
        if not Data:
            break
        else:
            hobj.update(Data)
            fobj.close()

            return hobj.hexdigest()
  


def BackupFiles(Source,Destination):
    copied_files = []

    lobj.write(Border+"\n")
    lobj.write("Creating a Backup folder for backup process\n")
    lobj.write(Border+"\n")

    os.makedirs(Destination,exist_ok=True)
    EXCLUDE_EXTENSIONS = (".tmp", ".log", ".exe")

    for root,dirs,files in os.walk(Source):
        for file in files:
            if file.endswith(EXCLUDE_EXTENSIONS): 
                continue
            src_path=os.path.join(root,file)

            relative = os.path.relpath(src_path,Source)
            dest_path = os.path.join(Destination,relative)

            os.makedirs(os.path.dirname(dest_path),exist_ok=True)

            #Copy the if its new

            if((not os.path.exists(dest_path))or (calculate_hash(src_path)!= calculate_hash(dest_path))):
            
                shutil.copy2(src_path,dest_path)
                copied_files.append(relative)
                lobj.write("Backup Filename : "+file+"\n")
    return copied_files


   

def MarvellousDataShieldStart(Source="Data"):
    
    global lobj
    lobj = Logfilecreation()

    Border ="-"*50
    BackupName="MarvellousBackup"

    
    lobj.write(Border+"\n")
    lobj.write("Backup Process Started Successfully at :"+time.ctime()+"\n")
    lobj.write(Border+"\n")

    files = BackupFiles(Source,BackupName)
    zip_file = make_zip(BackupName)
    update_history(zip_file,len(files))

    lobj.write("\n"+Border+"\n")
    lobj.write("Backup Completed Successfully\n")
    lobj.write(f"Files copied {len(files)}\n")
    lobj.write(Border+"\n")
    lobj.write("\n Zip file gets created : "+zip_file+"\n")
    lobj.write(Border+"\n")
    
    lobj.write(Border+"\n")
    lobj.write("\n")
    lobj.write(Border+"\n")

    lobj.close()
    return lobj.name, zip_file
    
def main():
    
     # Always use separate temporary/testing account
    sender_email = "shreelekhabamane271198@gmail.com"

    # App password generated from Google account
    app_password = "ixmr iywk uxhn icwf"

    # Your second email for testing
    receiver_email = "shreelekhabamane27@gmail.com"

    subject = "Marvellous Data Shield System Log and Backup Inventory"

    body = """Hello team,

    This email is showcase report of Data shield inventory.
    PFA log details and and file backup details

    Regards,
    Marvellous Infosystems
    """
    
    

    print("Marvellous Mail Sent Successfully")
    
    Border ="-"*50

    print(Border)
    print("-------Marvellous Data Shield System---------------")
    print(Border)

    if (len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This script is use to :")
            print("1 : Take Auto Backup at given time ")
            print("2 : Backup only new and updated files")
            print("3 : Create and archive of the backup periodically")
            

        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Use the Automation script as ")
            print("Scriptname.py TimeInterval SourceDirectory")
            print("TimeInterval : The time in minutes for periodic scheduling")
            print("SourceDirectory : Name of directory to backed up")

        elif(sys.argv[1]=="--history"): 
            show_history()
    
        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")
    
    #Pythin Demo.py 5 Data
    
    elif(len(sys.argv)==3):
        print("Inside Project Logic")
        print("Time Interval :",sys.argv[1])
        print("Directory name :",sys.argv[2])
        
        #Apply the schedular
        
        schedule.every(int(sys.argv[1])).minutes.do(lambda: SendMail(sender_email,app_password,receiver_email,subject,body,list(MarvellousDataShieldStart(sys.argv[2]))))

        print(Border)
        print("Marvellous Data Sheild System started successfully")
        print("Time Interval in minutes: ",sys.argv[1])
        print("Press Ctrl + C to stop the execution")
        print
        # Wait till Abort
        while True:
            schedule.run_pending()
            time.sleep(1)
            
    elif(len(sys.argv)==4 and sys.argv[1]=="--restore"): 
        zip_file = sys.argv[2] 
        destination = sys.argv[3] 
        RestoreBackup(zip_file, destination)

    
    else:
        
        print("Invalid Number of command line argument")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details")    
    
    print(Border)
    print("----------Thank You For Using Our Script----------")
    print(Border)

if __name__=="__main__":
    main()