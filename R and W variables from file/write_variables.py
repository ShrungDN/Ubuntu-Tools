# Shrung D N, ME19B168
# Assignment 5, q3

# Initialize variables
X = [1.1, 2.2, 3.3, 4.4, 5.5]
S = "Authentication code for this file is XzmBqr"
P = {'model':'Avrami', 'n':4, 'A':1.05, 'system':'sample binary'}
Q = [[1.1, 1.2, 1.3],[2.1, 2.2, 2.3],[3.1, 3.2, 3.3]]
# X and Q are both stored as lists, however Q can be interpreted as
# a matrix as it contains lists inside a list 

# List of variables to be written to file 
variables_to_write = ['X', 'S', 'P', 'Q']
variables_written = []

# Opening file in write mode
with open('data.dat', 'w') as fh:
    # var - contains variable name as string 
    # val - contains value of variable in appropriate data type
    # each 'if statement' checks the type of variable and writes it into
    # the data file after making the appropriate changes in the string 
    # so that octave and python can read the data file easily
    for var in variables_to_write:
        val = eval(var)

        # Checks if variable is a string 
        if isinstance(val, str):
            fh.write(f"string;{var};'{val}'\n")
            variables_written.append(var)
            continue

        # Checks if variable is a list        
        elif isinstance(val, list):
            try:
                # If no error is thrown here, it means that the list
                # has sub-lists, i.e, it is a matrix
                rows = len(val)
                cols = len(val[0])
            except:
                # This is executed if there is an error in 'try:', i.e, 
                # the list is not a matrix, and these statements are run
                rows = 1
                cols = len(val)
            fh.write(f"list;{var};{val};{rows};{cols}\n")
            variables_written.append(var)
            continue 

        # Checks if the variable is a dictionary (structure in octave)
        elif isinstance(val, dict):
            n = len(val)
            fh.write(f"struct;{var};{n}")
            # p is taken to be a string as in octave, dictionary field
            # names must be strings
            for p,q in val.items():
                if isinstance(q, str):
                    fh.write(f";{p}='{q}'")
                else:
                    fh.write(f";{p}={q}")
            fh.write("\n")
            variables_written.append(var)
            continue
            
        else:
            print("Problem writing variable")

print("Variables written:", end=" ")
for i in variables_written:
    print(i, end=" ")
print("")