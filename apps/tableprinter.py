# desc of goal here: https://automatetheboringstuff.com/2e/chapter6/
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(input_data):
    printStatement = """"""
    transposed_list = []
    colWidths = []
    for list in input_data:
        colWidths.append(len(max(list)))
    for index in range(0,len(input_data[0])):
        tmp_list = []
        for list in input_data:
            tmp_list.append(list[index])
        transposed_list.append(tmp_list)
    for row in transposed_list:
        printStatement += '\n'
        for index in range(0,len(colWidths)):
            printStatement += (row[index].rjust(colWidths[index]+1))
    printStatement += '\n'    
    print printStatement
printTable(tableData)


