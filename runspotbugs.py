# @author: zgjoget9
   # @Date: 2021/3/20
   # @Time: 00:01:01
   # @File: runspotbugs.py
import os
def main():
    work_dir = os.getcwd()
    all_proj= os.listdir(work_dir)
    for i in all_proj:
        j=1
        if os.path.isdir(i):
            proj = i
            print(i+"/jars.txt")
            rf=open(i+"/jars.txt","r")
            line=rf.readline()
            line=line[0:-1]
            while line:
               
                (path , filename) = os.path.split(line)
                with open(str(path)+"/finalxml.txt","w") as wf:
                    wf.write(line)
                #run spotbugs
                cmd = "java -Xmx16384m -jar YOUR_SPOTBUGS_LOCATION_SUCH_AS(/..../spotbugs-4.2.2/lib/spotbugs.jar) -textui -analyzeFromFile " + str(path) + "/finalxml.txt -xml -output "+ "YOUR_PORJECT_PATH/allxml/" + proj+ str(j)+ ".xml -low -effort:max"
                
                j+=1
                os.system(cmd)
                line=rf.readline()
                line=line[0:-1]
            rf.close()
  
 
 
  
  
if __name__ == "__main__":
       main()

