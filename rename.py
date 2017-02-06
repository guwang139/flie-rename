#*-*coding:utf8*-*
import os
import time
import re

def dir_files(dir_path):                                              #get files belong to this dir
    worker_dir = dir_path
    worker_dir_files = os.listdir(worker_dir)
    print 'worker dir is : %s ' %(worker_dir)
    print '#'*5 +'worker dir has files :  ' + '#'*5 
    for i in worker_dir_files:
        print i
    print '#'*5 +'END !! ' + '#'*5
    return worker_dir_files

def create_name(old_files,changename):
    f_dict = {}
    for i in old_files:                                                 #perview
        print '%s -----> %s' %(i,changename+i)
        f_dict[i]=changename+i
    return f_dict

def append_name(f_path,f_dict):                                               #append a string to old filename 
    op_history=open('append_rename.log','a+')
    op_history.write('#'*5 + time.ctime() + '#'*5 + changename+ '#'*5 +'\n')  
    for old in f_dict:
        try:
            os.rename(os.path.join(f_path,old),os.path.join(f_path,f_dict[old]))
            print '%s file name has been changed' %f_dict[old]
            op_history.write(os.path.join(f_path,old)+'\n')
        except Exception, e:
            print e
    op_history.close()
    
def rollback_name(f_path,backnum):
    files=dir_files(f_path)
    for file in files:
        name = os.path.join(f_path,file[backnum:])
        old_name = os.path.join(f_path,file)
        try: 
            os.rename(old_name,name)
            print '%s is ok !' %file[backnum:]
        except Exception, e:
            print e        

    
if __name__ == '__main__':
    print 'current dir : %s' %(os.getcwd())
    op_recoder=[]
    while True:
        f_path=raw_input('In put path :')
        old_files=dir_files(f_path)
        changename=raw_input('string append to file name: ')
        f_dict=create_name(old_files,changename)
        
        u_choice=raw_input(r'will you sure chang files name ?(y/n)')
        if u_choice=='y':   #run
            append_name(f_path,f_dict)
            op_recoder.append('+'+changename)
            
        if raw_input('do you want to back ?(y/n)')=='y':
            while True:
                try :
                    backnum = raw_input('How many number string do you want to del ?')
                    rollback_name(f_path,int(backnum))
                    break
                except Exception,e:
                    print e
            op_recoder.append('-'+backnum)
            
        print op_recoder
#            dir_files(f_path)

