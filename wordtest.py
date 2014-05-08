#!/usr/bin/python
# encoding=utf-8

import win32com.client
import os
   
class easyword:
    def __init__(self, filename = None):
        self.wordapp = win32com.client.gencache.EnsureDispatch("Word.Application")
        self.wordapp.Visible = 1
        if filename:
            self.filename = os.path.abspath(filename)
            self.wordapp.Documents.Open(self.filename)

    def Save(self, file_):
        if file_:
            path = os.path.abspath(file_)
            self.wordapp.ActiveDocument.SaveAs(path)
        else:
            self.wordapp.ActiveDocument.Save()

    def Find(self, findstr):
        self.wordapp.Selection.Find.Wrap = 1
        self.wordapp.Selection.Find.Execute(findstr)

    def Replace(self, src, dst):
        wdFindContinue = 1
        wdReplaceAll = 2
        find_str = src
        replace_str = dst
        self.wordapp.Selection.Find.Execute(find_str, False, False, False, False, False, \
                True, wdFindContinue, False, replace_str, wdReplaceAll)

    def close(self):
        self.wordapp.ActiveWindow.Close()

    def MoveRight(self, step = 1):
        self.wordapp.Selection.MoveRight(1,step)

    def MoveLeft(self, step = 1):
        self.wordapp.Selection.MoveLeft(1,step)

    def MoveUp(self):
        self.wordapp.Selection.MoveUp()

    def MoveDown(self):
        self.wordapp.Selection.MoveDown()

    def HomeKey(self):
        self.wordapp.Selection.HomeKey()

    def EndKey(self):
        self.wordapp.Selection.EndKey()

    def EscapeKey(self):
        self.wordapp.Selection.EscapeKey()

    def Delete(self):
        self.wordapp.Selection.Delete ()

    def SelectCell(self):
        self.wordapp.Selection.SelectCell()

    def Copy(self):
        self.wordapp.Selection.Copy()

    def Paste(self):
        self.wordapp.Selection.Paste()

    def TypeText(self,text):
        self.wordapp.Selection.TypeText(text)

    def CellRight(self):
        self.EndKey()
        self.MoveRight()

    def CellLeft(self):
        self.HomeKey()
        self.MoveLeft()

    def DelThenFillCell(self,text):
        self.SelectCell()
        self.Delete()
        self.TypeText(text)

    def InsertRowBelow(self):
        self.wordapp.Selection.InsertRowsBelow()

    def SetTableValue(self, tableid, row, col, value):
        self.wordapp.ActiveDocument.Tables(tableid).Cell(row,col).Range.Text = value

    def GetTableValue(self, tableid, row, col, value):
        return self.wordapp.ActiveDocument.Tables(tableid).Cell(row,col).Range.Text

    def GetTableRange(self, tableid, row1, col1, row2, col2):
        cell1 = self.wordapp.ActiveDocument.Tables(tableid).Cell(row1,col1)
        cell2 = self.wordapp.ActiveDocument.Tables(tableid).Cell(row2,col2)
        range = self.wordapp.ActiveDocument.Range(cell1.Range.Start, cell2.Range.Start)
        return range

    def GetCellByCotent(self, text):
        pass
        #return Range

    def Close(self):
        self.wordapp.ActiveWindow.Close()
        self.wordapp.Quit()

if __name__ == "__main__":
    wd = easyword("f:/baiduyun/python/wr.doc")
    wd.Replace("$year",'2014')
    wd.Replace("$week",'23')
    tab = wd.wordapp.ActiveDocument.Tables(1)
    range = wd.GetTableRange(1, 4, 1, 4, 1)
    range.Select()
    wd.InsertRowBelow()
    wd.SetTableValue(1,5,1,"1.")
    wd.SetTableValue(1,5,2,u"完成内容1")
    wd.SetTableValue(1,5,3,u"完成。")
    wd.InsertRowBelow()
    wd.SetTableValue(1,6,1,"2.")
    wd.SetTableValue(1,6,2,u"完成内容2")
    wd.SetTableValue(1,6,3,u"下周完成。")
    # wd.SetTableValue(
    # wd.SetTableValue(1, 1, 1, '123123123') 
    #wd.wordapp.ActiveDocument.Range(tab.Cell(1,1).Range.Start,tab.Cell(1,2).Range.End)
    #wd.MoveRight(5)
    #wd.SetTableValue(1,1,1,'dfd')
    #sel = range.Select()
    wd.Save("")
    wd.Close()
    # wd.selection.InsertRowsBelow()
    # wd.wordapp.ActiveDocument.Tables(1).Rows(17).Select
    # wd.selection.InsertRowsAfter()
