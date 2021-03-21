# Scripts_for_spotbugs
Scan all *souces.jar corresponding to *.jar in the current directory  
and each *jar output a xml file,then you can do something to the output xml file   
Here I provide information filtering on XML files   
## preparation 
1. you have to cd to the path you wanna spotbugs  
2. mkdir allxml
3. modify to your local path in the py files

## search .jar files
please ensure mkdir allxml
```
python3 pro2jars
```
this way we will search all *.jar files in the directory and save their path to jars.txt
## spotbugs 
it will take the longest time which decides on the number of *.jar you wanna search
```
python3 runspotbugs.py
```
## filter
here i will filter the xml files and output txt files and txt likes:


run 
```
python3 xmlfilter.py
```
