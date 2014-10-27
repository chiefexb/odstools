#!/usr/bin/python
#coding: utf8
from datetime import datetime
from odf.opendocument import OpenDocumentSpreadsheet
from odf.style import Style, TextProperties, ParagraphProperties, TableColumnProperties
from odf.text import P
from odf.table import Table, TableColumn, TableRow, TableCell
PWENC = "utf-8"
def initdoc():
 textdoc = OpenDocumentSpreadsheet()
 return textdoc
def inittable(textdoc):
 # Create a style for the table content. One we can modify
 # later in the word processor.
 tablecontents = Style(name="Table Contents", family="paragraph")
 tablecontents.addElement(ParagraphProperties(numberlines="false", linenumber="0"))
 tablecontents.addElement(TextProperties(fontweight="bold"))
 textdoc.styles.addElement(tablecontents)
 table = Table( name='test' )
 return table,tablecontents
def addrow(row,table,tablecontents):
 tr = TableRow()
 table.addElement(tr)
 for rr in row:
  if  str(type(rr))=="<type 'unicode'>":
   tc = TableCell(valuetype="string")
   tr.addElement(tc)
   p = P(stylename=tablecontents,text=rr)
   tc.addElement(p)
  elif  str(type(rr))=="<type 'float'>" or str(type(rr))=="<type 'int'>":
   tc = TableCell(valuetype="float",value=rr)
   tr.addElement(tc)
  elif str(type(rr))=="<type 'datetime.datetime'>":
   tc = TableCell(valuetype="string")
   tr.addElement(tc)
   p = P(stylename=tablecontents,text=unicode(rr.strftime("%d.%m.%Y") ,PWENC))
   tc.addElement(p)

  else:
   tc = TableCell(valuetype="string")
   tr.addElement(tc)
   p = P(stylename=tablecontents,text=unicode(rr,PWENC))
   tc.addElement(p)
 tr.addElement(tc)

 tr.addElement(tc)
 return table
def savetable(table,textdoc,filename):
 textdoc.spreadsheet.addElement(table)
 textdoc.save(filename)
 return
def main():
 return
if __name__ == "__main__":
    main()
