from colorama import Fore

def fileReader(fileName) -> list:
    
    with open(file=fileName, mode="r+") as openedFile:
        return openedFile.readlines()

def compareFiles(file1, file2, grouping=5) -> bool:
    
    fileMatch = True
    
    for index, (fileItem_1, fileItem_2) in enumerate(zip(file1, file2)):
        
        if fileItem_1 != fileItem_2:
            
            fileMatch = False
                        
            lowerLimit = max(0, index - grouping) 
            upperLimit = min(len(file1), index + grouping+1)

            file_1_itemGrouping = file1[lowerLimit:upperLimit]
            file_2_itemGroiping = file2[lowerLimit:upperLimit]
            
            for item in file_1_itemGrouping:
                print(Fore.GREEN+item.strip())
            print('\n')
            
            for item in file_2_itemGroiping:
                print(Fore.RED+item.strip())
            print('\n\n\n\n')
            
        else:
            continue
    
    return fileMatch    

__file1__ = fileReader("file1.txt")
__file2__ = fileReader("file2.txt")

print(compareFiles(file1=__file1__, file2=__file2__))
