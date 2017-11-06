# Assignment Rule Data Compression

## What does this Repository contain?

### ExampleDataset.csv
This repository contains a raw CSV file that represents table of meant for explicit assignments. 

The columns in the data set are:
   - Department
   - Country
   - City
   - Building
   - Branch
   - Assignment Group

When an assignnment is needed, there is a query to find the assignment that must be an exact match to the rule. This has several disadvantages: 
 - A record must exist for every unique combination of department, country, city, building, and branch. 
 - If a query has any error, it won't return any assignment

The result is a large dataset which is extremely sensitive to errors. 

### main.py
This file opens csv file and stores it in a dataframe, calls the compression function, and saves the file as a new csv. 

### assignmentCompression.py
This file contains a variety of functions that represent a recursive algorithm to compress the data set. The resulting data set allows default assignments to be set at lower levels which can be overridden with a higher level assignment. This table is significant reduction is size and the result query always returns an assignment group no matter the query.

### tester.py
This file contains a test that that compares the results of the new table with the assignments of the original table. 

## Results:
The compression algorithm takes ~9.16 seconds to compress the original 7785 records with 8gb ram and 3GHz processor Windows machine. The tester.py results shows the new table is 100% accurate. The new table size can vary as there are ties in the most frequent value in some parts of the data set. The lowest count was 735 records and the highest was 747 records. So, the new table both perfectly represents the old table, but it is also ~90% smaller. 

