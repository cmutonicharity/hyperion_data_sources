# Data Source
## Table of contents
1. Installation
2. Running the scripts
3. Task 1 - JSON
4. Task 2 - XML
## Installation
This project uses Python to execute the scripts. To use these scripts first ensure that you have python installed on your
computer. You can check this by running `python -v`. For further information on installing Python see: [python.org](https://www.python.org)
## Running the scripts
Once you have python installed, you can run these scripts on the command line with: `python ./taskXML.py`, or `xmlExample.py`.
### taskXML.py output
![Screenshot 2023-08-16 at 14 44 00](https://github.com/cmutonicharity/hyperion_data_sources/assets/133023982/17b0d830-a353-418e-b224-6d2690b008f6)
### xmlExample.py output
![Screenshot 2023-08-16 at 14 46 08](https://github.com/cmutonicharity/hyperion_data_sources/assets/133023982/d5be92df-4339-4594-8a1a-79b52111fc92)

## Task 1- In this project we used JSON to represent structured data. JSON stands for JavaScript.
* It is a syntax used for storing and exchanging unstructured data. The syntax for JSON is similar to Pyhon dictionary.
* Task 1 project involved populating file with data about books. 6 books were chosen and four attributes were chosen (author,date published,name of the book, genre )
## Task 2- is about parsing an XML file using python. 
* XML stands for eXtensible markup Language.
1. Project involved creating TaskXML.py
2. Importing xml.etree.Element as ET 
* Parsing XML file that contains data about movies. Listed all the child tags of the movie, printing out the movie titles and counting the number favourite and non-favourite movie.
###### Why is XML files Important?
* XML files are used to store data used by the data scientist and as a data scientist it is important to understand how to work with XML so that you can parse that data contained in XML files.
###### Why are JSON important?
* JSON are commonly used dealing with application programming interfaces. Some companies like Amazon can release their APIs tp tje public and other software developers can design software hat is powered by API services.
* 
| Type of Data Source | Description                                                                      |
|---------------------|----------------------------------------------------------------------------------|
| JSON                | Converting Python to JSON to populate file with data about books using JSON.     |
| XML                 | Parsing XML file that contains movie's and list all the child tags of the movie. |
