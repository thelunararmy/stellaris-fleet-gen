'''
@author: thelunararmy
'''

# Fleet variables to create, it should be straight forward
# The format for this is:
# Variable = [ "filename", [ ("shipname", value), ("shipname", value)... etc   ] ]
fanaticMaterialist = ["FM",[("Alpha",1),("Beta",50),("Gamma",100)]]
fanaticSpiritualist = ["FS",[("Eternal",1),("Avatar",50),("Zealot",100)]]
fanaticXenophile = ["FX1",[("Keeper",1),("Custodian",50),("Warden",100)]]
fanaticXenophobe = ["FX2",[("Imperium",1),("Supremacy",50),("Glory",100)]]

# In this variable you want to list all the fleet spawning files you want to make, add/remove any variables from above to suit your needs!
make_this = [fanaticMaterialist,fanaticSpiritualist,fanaticXenophile,fanaticXenophobe]

# This function does all the heavy lifting for you
def PopulateShips (data):
    finale = []
    for ship,value in data:
        for _ in range(value):
            finale.append("add_ship %s"%(ship))
    return '\n'.join(finale)

# This where the program executes
if __name__ == '__main__':
    print "Writing scripts"
    for name, data in make_this:
        # Every fleet variable will be saved as a spawnFleetname.txt in the same folder as this script
        with open('spawn'+name+'.txt','w') as f:
            f.write(PopulateShips(data))
        f.close()
    print "Complete"
        