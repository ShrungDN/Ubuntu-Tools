# Shrung D N, ME19B168
# Assignment 5, q3

# List of variables read from file 
variables_read = []

# Opening file in read mode 
with open("data.dat",'r') as fh:
    # Each record(line) in the data file is processed appropriately 
    # in the following if statements based on its data type
    for rec in fh:
        rec = rec[:-1]
        rec = rec.split(';')

        # Checks if the variable is a string 
        if rec[0]=='string':
            cmd = "%s = %s" % (rec[1],rec[2])
            exec(cmd)
            variables_read.append(rec[1])

        # Checks if the variable is a list 
        elif rec[0]=='list':
            cmd = "%s = %s" % (rec[1],rec[2])
            exec(cmd)
            variables_read.append(rec[1])

        # Checks if the variable is a dictionary (structure in Octave)
        elif rec[0]=='struct':
            n = int(rec[2])
            cmd = "%s = {}" % (rec[1])
            exec(cmd)
            for i in range(n):
                temp = "%s" % (rec[i+3])
                temp = temp.replace("=","']=")
                cmd = "%s['%s" % (rec[1],temp)
                exec(cmd)
            variables_read.append(rec[1])

        else:
            print("Variable could not be laoded: ", rec[1])

# Prints all the variables read and its value along with its data type
# It shows matrix as list because matrix is a list of lists
print("Variables read:")
for i in variables_read:
    print(i," = ", eval(i), "    ", type(eval(i)))
