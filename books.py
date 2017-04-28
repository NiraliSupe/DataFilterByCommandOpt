import sys, csv
import argparse

class books(object):
    def __init__(self):
        self.filedata  = [] 
		
    def readFilesAndSortByYear(self):
        '''
        Read input files and sort by last name
        Output format : Last name, First name, Book Title, Book Publication
        '''
        self.readPipeFile()
        self.readSlashFile()
        self.readCSVFile()
        self.filedata.sort(key=lambda ele: ele[0].strip(' '))
		
    def readPipeFile(self):
        '''
        Pipe file format : First name | Last name | Book Title | Book Publication 
        Read the file and conver to output format
        '''		
        print (" ** Retrieving Pipe file data...")
        pipe_file      = open('pipe', 'r')
        pipe_data      = csv.reader(pipe_file, delimiter="|")
        for data in pipe_data:
            data[0], data[1] = data[1], data[0]
            self.filedata.append(data)
		
    def readSlashFile(self):
        '''
        Slash file format : Book Publication Date/First name/Last name/Book Title
        Read the file and conver to output format
        '''		
        print (" ** Retrieving Slash file data...")
        slash_file     = open('slash', 'r')
        slash_data     = csv.reader(slash_file, delimiter="/")
        for data in slash_data:
            data.append(data[0])
            data[1], data[2] = data[2], data[1]
            data.pop(0)
            self.filedata.append(data)
		
    def readCSVFile(self):
        '''
        Slash file format : Book Title, Last Name, First name, Book Publication Date
        Read the file and conver to output format
        '''	
        print (" ** Retrieving csv file data...")
        csv_file       = open('csv', 'r')
        csv_data       = csv.reader(csv_file, delimiter=",")
        for data in csv_data:
            data[0], data[2] = data[2], data[0]
            self.filedata.append(data)

    def filter(self, filter_val=None, order=None):
        '''
        Read the files, merge the data and sort by last name
        If filter value is not provided or if provided and it is present in the row,
        then store in the result else skip the row
        If order == year then sort books by year and display
        If order == reverse then reverse the sort (sort by last name) and display		
        '''
        self.readFilesAndSortByYear()
        result = []
        for row in self.filedata:
            row    = ",".join([ele.rstrip(' ') for ele in row])
            if (filter_val is None) or (filter_val in row):
                result.append(row.lstrip())
        if order == 'year':
            result.sort(key=lambda ele: int(ele.split(',')[3]))
        elif order == 'reverse':
            result.reverse()

        self.displayResult(result)
				
    def displayResult(self, result):
	    print ( "\n".join(result))

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='FilterAndSort')
    parser.add_argument('--filter' , nargs=1            , help='Show a subset of books, looks for the argument as a substring of any of the fields' )
    parser.add_argument('--reverse', action='store_true', help='Reverse sort' )
    parser.add_argument('--year'   , action='store_true', help='Sort the books by year ascending' )
    args = parser.parse_args()

    b = books()

    if (args.filter is not None) and (args.year):
        b.filter(args.filter[0], 'year')	
    elif (args.filter is not None and (args.reverse)):
        b.filter(args.filter[0], 'reverse')
    elif (not args.reverse) and (not args.year):
        if args.filter is None:
            b.filter()
        else:
            b.filter(args.filter[0])
		
    sys.exit(0)