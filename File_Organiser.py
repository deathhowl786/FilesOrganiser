import os
import shutil

def organiser():

    # Taking working directory
    root_directory = input("Enter Path of Directory = ")
    # changing directory to working directory
    os.chdir(root_directory)
    # Parsing through all the files in the directory 
    for dirpath, dirnames, filenames in os.walk(f'{root_directory}'):
    # Working on each file in the directory
        for file in filenames:
        # checking the extension of the file
            extension = os.path.splitext(f'{file}')[1]
        # making a directory path in the name of the extension within the working directory
            file_Npath =  os.path.join(os.getcwd(), extension)
        # checking if directory path exists, if not then creating one
            if(os.path.exists(file_Npath)):
                pass
            else:
                os.mkdir(f'{extension}')
        
        # shifting the file to the directory with the name of its extension 
            shutil.move(os.path.join(root_directory,file), os.path.join(file_Npath, file))
        # breaking to avoid the loop to go into sub directories
        break
    print(f"{os.path.split(root_directory)[1]} Directory has been Organised Successfully.\n")


def main():
    flag = 1
    while(flag):
        try:
            organiser()
        except Exception as e:
            print("\nCouldn't Process.")
            print("1. Don't include Quotation marks while entering path.")
            print("2. Provide a path which exists and points to an Actual Directory.") 
            print("3. Don't Provide file paths.")
            print("4. Avoid putting spaces in the front or end.")
            print(f"Error : {e}.\n")   

        flag = int(input("Enter 1 to Continue = "))


if(__name__ == '__main__'):
    main()

