from xml.dom.minidom import parse
import xml.dom.minidom
import os
import sys
# using minidom 


typelist = ['BC_UNCONFIRMED_CAST', 'DLS_DEAD_LOCAL_STORE', 'RCN_REDUNDANT_NULLCHECK_OF_NONNULL_VALUE', 'UCF_USELESS_CONTROL_FLOW', 'UWF_FIELD_NOT_INITIALIZED_IN_CONSTRUCTOR']

BC_UNCONFIRMED_CAST = []
DLS_DEAD_LOCAL_STORE = []
RCN_REDUNDANT_NULLCHECK_OF_NONNULL_VALUE = []
UCF_USELESS_CONTROL_FLOW = []
UWF_FIELD_NOT_INITIALIZED_IN_CONSTRUCTOR = []
filedir = "/.../allxml/"
files = os.listdir(filedir)
f1 = open("/.../BC_UNCONFIRMED_CAST.txt","w+")
f2 = open("/.../DLS_DEAD_LOCAL_STORE.txt","w+")
f3 = open("/.../RCN_REDUNDANT_NULLCHECK_OF_NONNULL_VALUE.txt","w+")
f4 = open("/.../UCF_USELESS_CONTROL_FLOW.txt","w+")
f5 = open("/.../UWF_FIELD_NOT_INITIALIZED_IN_CONSTRUCTOR.txt","w+")
for file in files:
    if not file.endswith('.xml'):
        continue
    try:
        DOMTree = xml.dom.minidom.parse(filedir+file)
    except:
        continue
    collection = DOMTree.documentElement
    jar = collection.getElementsByTagName("Jar")
    BugInstance = collection.getElementsByTagName("BugInstance")

    for buginstance in BugInstance:
        TYPE = buginstance.getAttribute("type")
        if TYPE not in typelist:
            continue
        entity = []
        signatures = []
        clasS = buginstance.getElementsByTagName("Class")
        for claSS in clasS:
            sourceline = claSS.getElementsByTagName("SourceLine")[0]
            entity.append("file: "+sourceline.getAttribute("sourcepath"))
        methods = buginstance.getElementsByTagName("Method")
        for method in methods:
            sourceline = method.getElementsByTagName("SourceLine")[0]
            entity.append("method name: " + method.getAttribute("name"))
            entity.append("method signature: " + method.getAttribute("signature"))
            entity.append("method begin: "+sourceline.getAttribute("start"))
            entity.append("method end: " + sourceline.getAttribute("end"))
        sourcelines = buginstance.childNodes
        i = len(sourcelines)-1

        while(i>=0):
            if sourcelines[i].localName=="SourceLine":
                entity.append("bug begin: " + sourcelines[i].getAttribute("start"))
                entity.append("bug end: " + sourcelines[i].getAttribute("end"))
            i-=1
        if TYPE == 'BC_UNCONFIRMED_CAST':
            if entity not in BC_UNCONFIRMED_CAST:
                BC_UNCONFIRMED_CAST.append(entity)
                f1.writelines("jar: "+jar[0].childNodes[0].data+'\n')
                for i in entity:
                    f1.writelines(i+'\n')
                f1.writelines('\n')
        elif TYPE == 'DLS_DEAD_LOCAL_STORE':
            if entity not in DLS_DEAD_LOCAL_STORE:
                DLS_DEAD_LOCAL_STORE.append(entity)
                f2.writelines("jar: " + jar[0].childNodes[0].data+'\n')
                for i in entity:
                    f2.writelines(i+'\n')
                f2.writelines('\n')
        elif TYPE == 'RCN_REDUNDANT_NULLCHECK_OF_NONNULL_VALUE':
            if entity not in RCN_REDUNDANT_NULLCHECK_OF_NONNULL_VALUE:
                RCN_REDUNDANT_NULLCHECK_OF_NONNULL_VALUE.append(entity)
                f3.writelines("jar: " + jar[0].childNodes[0].data+'\n')
                for i in entity:
                    f3.writelines(i+'\n')
                f3.writelines('\n')
        elif TYPE == 'UCF_USELESS_CONTROL_FLOW':
            if entity not in UCF_USELESS_CONTROL_FLOW:
                UCF_USELESS_CONTROL_FLOW.append(entity)
                f4.writelines("jar: " + jar[0].childNodes[0].data+'\n')
                for i in entity:
                    f4.writelines(i+'\n')
                f4.writelines('\n')
        elif TYPE == 'UWF_FIELD_NOT_INITIALIZED_IN_CONSTRUCTOR':
            if entity not in UWF_FIELD_NOT_INITIALIZED_IN_CONSTRUCTOR:
                UWF_FIELD_NOT_INITIALIZED_IN_CONSTRUCTOR.append(entity)
                f5.writelines("jar: " + jar[0].childNodes[0].data+'\n')
                for i in entity:
                    f5.writelines(i+'\n')
                f5.writelines('\n')
print('over')
f1.close()
f2.close()
f3.close()
f4.close()
f5.close()

