import DecisionTree


def main():
    """
    IMPORTANT: Change this file path to change training data
    """
    trainingFile = 'SoybeanTraining'
    """
    IMPORTANT: Change this file path to change testing data 
    """
    dataFile = 'Soybean'
    # Insert input file
    file = open('data/{0}.csv'.format(trainingFile))
    """
    IMPORTANT: Change this variable too change target attribute 
    """
    target = "class"
    data = [[]]
    for line in file:
        line = line.strip("\r\n")
        data.append(line.split(','))
    data.remove([])
    attributes = data[0]
    data.remove(attributes)
    # Run ID3
    tree = DecisionTree.makeTree(data, attributes, target, 0)
    print("generated decision tree")
    # Generate program
    file = open('program.py', 'w')
    file.write("import Node\n\n")
    # open input file
    file.write("data = [[]]\n")
    file.write("f = open('data/{0}.csv')\n".format(dataFile))
    # gather data
    file.write("for line in f:\n\tline = line.strip(\"\\r\\n\")\n\tdata.append(line.split(','))\n")
    file.write("data.remove([])\n")
    # input dictionary tree
    file.write("tree = %s\n" % str(tree))
    file.write("attributes = %s\n" % str(attributes))
    file.write("count = 0\n")
    file.write("for entry in data:\n")
    file.write("    count += 1\n")
    # copy dictionary
    file.write("    tempDict = tree.copy()\n")
    file.write("    result = \"\"\n")
    # generate actual tree
    file.write("    while(isinstance(tempDict, dict)):\n")
    file.write("        tempKeys = list(tempDict.keys())\n")
    file.write("        root = Node.Node(tempKeys[0], tempDict[tempKeys[0]])\n")
    file.write("        tempDict = tempDict[tempKeys[0]]\n")
    # this must be attribute
    file.write("        index = attributes.index(root.value)\n")
    file.write("        value = entry[index]\n")
    # ensure that key exists
    file.write("        if(value in tempDict.keys()):\n")
    file.write("            child = Node.Node(value, tempDict[value])\n")
    file.write("            result = tempDict[value]\n")
    file.write("            tempDict = tempDict[value]\n")
    # otherwise, break
    file.write("        else:\n")
    file.write("            print (\"can't process input {0}\".format(count))\n")
    file.write("            result = \"?\"\n")
    file.write("            break\n")
    # print solutions
    file.write("    print (\"entry%s = %s\" % (count, result))\n")
    print("written program")


if __name__ == '__main__':
    main()
