PLACEHOLDER = '[name]'


with open('./Input/Names/invited_names.txt','r') as names:
    # returns each line as an item in a list
    namelist = names.readlines()

    

with open('./Input/Letters/starting_letter.txt','r') as letters:
    # reads all the content in a file
    letterlist = letters.read()

    for name in namelist:
        # strip() removes the leading and trailing whitespace
        __name__ = name.strip()
        # replaces PLACEHOLDER (that is currently in the file) with __name__
        new_letter = letterlist.replace(PLACEHOLDER,__name__)
        # write a new file with the name as part of the title
        with open(f"./Output/ReadyToSend/letter_for_{__name__}.txt",'w') as completed_letter:
            
            completed_letter.write(new_letter)
