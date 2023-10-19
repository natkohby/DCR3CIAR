def binary(a):
    return 2048*a[0]+1024*a[1]+512*a[2]+256*a[3]+128*a[4]+64*a[5]+32*a[6]+16*a[7]+8*a[8]+4*a[9]+2*a[10]+a[11]

def qt(a):
    return [a[3],a[4],a[5],a[11],a[10],a[9],a[2],a[1],a[0],a[6],a[7],a[8]]

def rf(a):
    return [a[0],a[1],a[2],a[8],a[7],a[6],a[5],a[4],a[3],a[9],a[10],a[11]]

def qt4(a):
    return [a[1],a[2],a[3],a[0]]

def rf4(a):
    return [a[0],a[3],a[2],a[1]]

def neighbourhood(a):
    return '...'+str(a[0])+'...\n...'+str(a[1])+'...\n...'+str(a[2])+'...\n'+str(a[3])+str(a[4])+str(a[5])+'X'+str(a[6])+str(a[7])+str(a[8])+'\n...'+str(a[9])+'...\n...'+str(a[10])+'...\n...'+str(a[11])+'...'

import csv
print('===================================================')
print('Durnak-Cole R3 Cross Isotropic Assistant Rulegolfer')
print('By Harsforden Parker-Cole and Haycat Durnak')
print('An interactive database of every R3 Cross transition')
print('===================================================')
print('I assume you came here because you knew about R3 Cross rules.')
print('There are 666 Cross transitions - devilishly difficult for a human to remember.')
print('That\'s why we made this to help you!')
print('Neighbourhoods are always entered in the form:')
print('...a...')
print('...b...')
print('...c...')
print('defXghi')
print('...j...')
print('...k...')
print('...l...')
print('where X is the central cell.\n\n')
print('An alluring feature of R3 Totalistic Cross rules is the existence of extensions.')
print('However, most non-INT R3 Cross rules do not ahve this property. However, some do - and these are called expandable.')
print('From a given transition, one can find the expansions and contractions, so that when you add all of them, you get this alluring property for one group of transitions!\n\n')
print('Semi-totalistic rules have the same number of edge and corner cells in Moore.')
print('However, we extend this definition to R3 Cross stating that there have to be the same number of inner, middle, and outer cells.')
print('From a given transition, one can find the group of semi-totalistic-equivalent transitions containing one transition.\n\n')


status = input('Do you want to start the Assistant Rulegolfer? Y (Yes)/N (No) ')

while status.lower() == 'y':

    trans = []

    transitions = open('data.csv')

    csvreader = csv.reader(transitions)

    for row in csvreader:
        trans.append(row)

    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    c = int(input('Enter c: '))
    d = int(input('Enter d: '))
    e = int(input('Enter e: '))
    f = int(input('Enter f: '))
    g = int(input('Enter g: '))
    h = int(input('Enter h: '))
    i = int(input('Enter i: '))
    j = int(input('Enter j: '))
    k = int(input('Enter k: '))
    l = int(input('Enter l: '))

    iden = [a,b,c,d,e,f,g,h,i,j,k,l]

    confirm = input('Your neighbourhood is \n'+neighbourhood(iden)+'\nConfirm? Y (Yes)/N (No) ')
    if confirm.lower() == 'y':

            transform = [iden,qt(iden),qt(qt(iden)),qt(qt(qt(iden))),rf(iden),rf(qt(iden)),rf(qt(qt(iden))),rf(qt(qt(qt(iden))))]

            binar = []

            for i in range(0, len(transform)):
                binar.append(binary(transform[i]))

            minnum = min(binar)

            for i in range(0, len(trans)):
                if trans[i][-1] == str(minnum):
                    print('Your transition is: '+trans[i][0])
                    transitionnum = i

            expandableinput = input('Would you like expansions/contractions with that? Y (Yes)/N (No)')
            if expandableinput.lower() == 'y':
                expand = [trans[transitionnum][1],trans[transitionnum][2],trans[transitionnum][4],trans[transitionnum][3]]
                print('Your expanded transitions are: ')
                expandperm = [expand,qt4(expand),qt4(qt4(expand)),qt4(qt4(qt4(expand))),rf4(expand),rf4(qt4(expand)),rf4(qt4(qt4(expand))),rf4(qt4(qt4(qt4(expand))))]
                for i in range(0, len(trans)):
                    if [trans[i][1],trans[i][2],trans[i][4],trans[i][3]] in expandperm:
                        print(trans[i][0])

            stotalisticinput = input('Would you like semitotalistic variants with that? Y (Yes)/N (No) ')
            if stotalisticinput.lower() == 'y':
                stotalistic = [trans[transitionnum][5],trans[transitionnum][6],trans[transitionnum][7]]
                print('Your semitotalistic variants are: ')
                for i in range(0, len(trans)):
                    if [trans[i][5],trans[i][6],trans[i][7]] == stotalistic:
                        print(trans[i][0])
            status = input('Try again? Y (Yes)/N (No) ')
    if confirm.lower() == 'n':
        status = 'Y'
