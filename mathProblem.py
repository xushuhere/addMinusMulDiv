import random, os, datetime
from webbrowser import open_new_tab

def mathProblem():
        a = "  ÷  "
        b = "  x  "
        c = "  +  "
        d = "  -  "
        res = " = _____ "
        result = []
        for i in range(1, 13):
            for j in range(1, 13):
                    # = 
                    #list2 = [str(i), b, str(j),res]
                result.append([str(i*j), a, str(j),res])

                result.append([str(i), b, str(j),res])


        for i in range(0, 21):
            for j in range(0, 21):
                    if i+ j <= 20:
                        result.append([str(i), c, str(j),res] )
                    if i >= j: 
                        result.append([str(i), d, str(j),res] )


        result = [tuple(t) for t in result]
        lst = random.sample(range(1, len(result)), 100)
        return result, lst
        
        # count = 0
        ## for j in lst:
        #    if count >=5:
        #        print("")
        #        count = 0
        #    count+=1
        #    print('{}{}{}{}\t'.format(result[j][0],result[j][1],result[j][2], result[j][3] ), end='\t')
            
        #print("")



# Given name of calling program, a url and a string to wrap,
# output string in html body with basic metadata and open in Firefox tab.

def wrapStringInHTMLMac(body):
    
    now = datetime.datetime.today().strftime("%Y%m%d-%H%M%S")
    filename = now + '.html'
    f = open('./toPrint/'+filename,'w')
    program=''
    url=''
    wrapper = """<html>
    <head>
    <title>%s output - %s</title>
    </head>
    <body>%s</body>
    </html>"""

    whole = wrapper %  (program, now,  body)
    f.write(whole)
    f.close()

    #Change the filepath variable below to match the location of your directory
    abspath = os.path.abspath('./')
    filename = 'file://' + abspath+ '/toPrint/'+ filename

    open_new_tab(filename)




def wrapInTab(result, lst):
    tableText = '<p></p>'
    tableText = tableText + '<p></p>'
    tableText = tableText + '<p>  Name: _______   Date: ___________   Score: _______</p>'
    tableText = tableText + '<p></p>'
    tableText = tableText + '<p></p>'
    tableText = tableText+ '<style>table, th, td {border: 1px dash black; border-spacing: 10px; align: right }</style>' + '<table ><tr>'
    count = 0
    for j in lst:
        if count >=5:
            tableText = tableText + '</tr> <tr>'
            count = 0
        count+=1
        tableText = tableText + '<td align="right">' + result[j][0]+ result[j][1]+ result[j][2]+ result[j][3] + '</td>'
                
    tableText = tableText + '</tr></table>'
    return tableText

result, lst = mathProblem()
body = wrapInTab(result, lst)
# print(body)
wrapStringInHTMLMac(body)
