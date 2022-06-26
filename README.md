# CLI-Copy
A command line program to copy files and folders according to Xml configuration files.

A cli version of [Deploy-Helper](https://github.com/albino98/deploy-helper) .

## Usage

1. Clone repository or download files into a folder.


2. Configure an xml file like following:


~~~ xml

<xml>
	<deploys>
		<deploy name="testFile">
			<sourceFilePath>/home/cartella</sourceFilePath>
			<sourceFilePath>/home/testFile.txt</sourceFilePath>
			
			<destinationPath>/home/destination</destinationPath>
			<backupPath>/home/backup</backupPath>
		</deploy>
	</deploys>
</xml>

~~~


3. Open cmd in the program folder and run:

~~~
 python3 main.py -d <xmlFileName>
~~~

   example:

~~~
 python3 main.py -d testFile
~~~
    
  :warning: Save the xml file with the same name as the deploy attribute. Example:
  
  ~~~ xml
  <deploy name="testFile">
   ~~~
   
   **File name:** testFile.xml
    
