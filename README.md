# python_cli
Work in Progress. Scripting reads/writes to CSV files with PYthon.

Man-like description of how to use program.

# This program was developed on macOS and a Windows equivalent was not available for testing. Instructions are directed towards Mac users but should be able to transfer to Windows and other OS’.

•	To get started first download the file and unzip it if compressed. Open your terminal. You can open this several ways using spotlight search and typing ‘terminal’ or opening Finder and traveling through the following file path: ‘Applications>Utilities>Terminal’
•	Once you have the terminal open you have to get to the directory with the files you previously downloaded. To do this use the Unix ‘cd’ command which is for Change Directory. For example, it might be by default in your ‘Downloads’ folder: ‘cd Downloads/’ should get you in there.
•	Once there you can run the utility by running the following command in your terminal:
‘python3 main.py’ Python 3 must be installed.

# Function tutorials (Read, Write, Update, Delete)
When you first run main.py you’ll get a prompt:
Hello welcome to this CSV app! First you'll need to specify a function read, write, update, & delete
Specify function (e.g. read, write, update, & delete):

# Write Function
Without a CSV file we can’t do anything so let’s first create one. 

OPTIONAL the CSV will create a few records of Michael Jordan’s stats from 1987-90. If you want to customize this, you can easily open the main.py and fill in the values.

Type in ‘write’ in the terminal. You should get a prompt like the following:
Enter file name (e.g test.csv):
The input here will be the name of the file. Once you click enter/return you should see a ‘filename.csv’ file appear in the same folder as ‘main.py’. Once open you’ll see CSVs.

# Read Function
You can also read the CSV file you just created and print all of its values on the terminal. Run ‘main.py’ again. This time when you get the prompt of specifying function type in ‘read’.

You should see a printed list of stats.

# Update Function
You can update a record. Run ‘main.py’ again. This time when you get the prompt of specifying function type in ‘update’.

You should get a prompt like the following:
Enter file name (e.g test.csv):

Enter ‘filename.csv’. Nothing will happen in the terminal but now open filename.csv and you should see a record change.


# Delete Function
You can remove a record. Run ‘main.py’ again. This time when you get the prompt of specifying function type in ‘delete’.

You should get a prompt like the following:
This will remove one PPG field
Enter a file name to update (e.g. test.csv):

Enter ‘filename.csv’. Nothing will happen in the terminal but now open filename.csv and you should see a record change.

