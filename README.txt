This was made for a larger project N.N.N. (See: https://github.com/Mar13554/N.N.N.-Neural-Network-Nexus)
You will need to run the file yourself (working on an .exe will probably not come)
Modules needed: PyQt5 

Current options for convertion:
  one-to-one (words)
  sentence-to-sentence
The code (as the name suggests) takes a paragraph and put out an I/O json file format of:
{
  "1":{
    "1":{
      "Input":"Text",
      "Output":"Text"}
    "2":{
      ...
      }
    ...
  }
} 
The json files will end up in the JSON folder (Keep the JSON folder with main.py).
If a .json file already exists the program will add the new I/O with it, if not a new file is created.

Last updated*: 11/12/24 (DD/MM/YYYY)
*For this ReadMe file ofcourse
