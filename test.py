#!/usr/bin/python
#coding: utf8
from odsmod import *
def main():
 textdoc=initdoc()
 table,tablecontents=inittable(textdoc)
 row=('123','1234')
 table=addrow(row,table,tablecontents)
 savetable(table,textdoc,'./1.ods')
# table.addElement(tr)
# tc = TableCell(valuetype="string")
# tr.addElement(tc)
# val='Тест'
# p = P(stylename=tablecontents,text=unicode(val,PWENC))
# tc.addElement(p)
# tc = TableCell(valuetype="float", value=0.54)
# tr.addElement(tc)
 #tc = TableCell(valuetype="string")
# tr.addElement(tc)
# val="05.12.2013"
# p = P(stylename=tablecontents,text=val)
# tc.addElement(p)
#
# tr.addElement(tc)
# textdoc.spreadsheet.addElement(table)
 textdoc.save('./1.ods' )

if __name__ == "__main__":
    main()
