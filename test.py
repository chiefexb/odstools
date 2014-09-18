#!/usr/bin/python
#coding: utf8
def main():
 PWENC = "utf-8"
 from odf.opendocument import OpenDocumentSpreadsheet
 from odf.style import Style, TextProperties, ParagraphProperties, TableColumnProperties
 from odf.text import P
 from odf.table import Table, TableColumn, TableRow, TableCell
 textdoc = OpenDocumentSpreadsheet()
 # Create a style for the table content. One we can modify
 # later in the word processor.
 tablecontents = Style(name="Table Contents", family="paragraph")
 tablecontents.addElement(ParagraphProperties(numberlines="false", linenumber="0"))
 tablecontents.addElement(TextProperties(fontweight="bold"))
 textdoc.styles.addElement(tablecontents)
 table = Table( name='test' )
 tr = TableRow()
 table.addElement(tr)
 tc = TableCell(valuetype="string")
 tr.addElement(tc)
 val='Тест'
 p = P(stylename=tablecontents,text=unicode(val,PWENC))
 tc.addElement(p)
 textdoc.spreadsheet.addElement(table)
 textdoc.save('./1.ods' )

if __name__ == "__main__":
    main()
