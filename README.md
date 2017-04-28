**Goal        :**  It is a python script that reads in records from various input files and then outputs the list with command line options to sort or filter them.                  

**Requirements:**                
Python 2.7     

**Options :**                 
-h, --help       show this help message and exit                
--filter FILTER  Show a subset of books, looks for the argument as a substring of any of the fields               
--reverse        Reverse sort               
--year           Sort the books by year ascending              

**Commands :**    
python books.py           
python books.py --filter 199          
python books.py --filter 199 --reverse         
python books.py --filter er --year                          