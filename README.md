# Scripts_for_spotbugs
Scan all *souces.jar corresponding to *.jar in the current directory  
and each *jar output a xml file,then you can do something to the output xml file   
Here I provide information filtering on XML files   
## preparation 
1. you have to cd to the path you wanna spotbugs  
2. mkdir allxml
3. modify to your local path in the py files like this:  
jar: /../springframework/boot/spring-boot-autoconfigure/2.1.2.RELEASE/spring-boot-autoconfigure-2.1.2.RELEASE.jar  
file: org/springframework/boot/autoconfigure/diagnostics/analyzer/NoSuchBeanDefinitionFailureAnalyzer.java  
method name: getFactoryMethodMetadata  
method signature: (Ljava/lang/String;)Lorg/springframework/core/type/MethodMetadata    
method begin: 156  
method end: 160  
bug begin: 156  
bug end: 156  

## search .jar files
please ensure mkdir allxml
```
python3 pro2jars.py
```
this way we will search all *.jar files in the directory and save their path to jars.txt
## spotbugs 
it will take the longest time which decides on the number of *.jar you wanna search
```
python3 runspotbugs.py
```
## filter
here i will filter the xml files and output txt files and txt likes:

![xmlfilter](https://github.com/zgjoget9/Scripts_for_spotbugs/blob/main/截屏2021-03-21%2012.22.29.png)

run `python3 xmlfilter.py`
