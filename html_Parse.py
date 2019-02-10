# HTMLParser
# An HTMLParser instance is fed HTML data and calls handler methods when start tags, end tags, text, comments, and other markup elements are encountered. 
# Task

# You are given an HTML code snippet of

# lines.
# YoOutput Format

# Print the HTML tags, attributes and attribute values in order of their occurrence from top to bottom in the given snippet.

# Use proper formatting as explained in the problem statement.ur task is to print start tags, end tags and empty tags separately.

# Format your results in the following way:
from html.parser import HTMLParser
import os

# create a subclass and override the handler methods
class MyHtmlParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start : " + tag)
        for xAttr in attrs:
            print('-> ' + str(xAttr[0]) + ' > ' + str(xAttr[1]))
            
    def handle_endtag(self, tag):
        print("End   : " + tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty : " + tag)
        for xAttr in attrs:
            print('-> ' + str(xAttr[0]) + ' > ' + str(xAttr[1]))
            
     def handle_comment(self, data):
        if data.rfind('\n') == -1:
            sComment = '>>> Single-line Comment'
        else:
            sComment = '>>> Multi-line Comment'
        print(sComment + "\n" + data)
  
    def handle_data(self, data):
        if data != '\n':
            print('>>> Data' + '\n' + data) 
        
import sys 
if __name__ == '__main__':
    cPath = os.getcwd()
    print(cPath)
    ficInput = open('html_test.txt', 'r')
    sHtml = ficInput.read()
    ##############
        n = int(input())
	  bCss = False
    for i in range(n):
        str_In = input()
        lColor = []
        if str_In.rfind('{') != -1:
            bCss = True
        if str_In.rfind('}') != -1:
            bCss = False 
        #print(str(i) + ' ' + str(bCss))
        if bCss :  
            #str_In = 'border-top: 20px solid #f00'
            lColor = re.findall('#+[a-fA-F0-9]+', str_In)
        for xColor in lColor:
            if len(xColor) == 4 or len(xColor) ==  7:
                print(xColor)
