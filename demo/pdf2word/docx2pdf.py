# -*- encoding:utf-8 -*-
"""
  author:lgh
"""

from win32com.client import Dispatch, constants, gencache

def doc2pdf(input, output):
    w = Dispatch('Word.Application')
    try:
        # 打开文件
        doc = w.Documents.Open(input, ReadOnly=1)
        # 转换文件
        doc.ExportAsFixedFormat(output, constants.wdExportFormatPDF,
                                Item=constants.wdExportDocumentWithMarkup,
                                CreateBookmarks=constants.wdExportCreateHeadingBookmarks)
        return True
    except:
        return False
    finally:
        w.Quit(constants.wdDoNotSaveChanges)


def GenerateSupport():
    gencache.EnsureModule('{00020905-0000-0000-C000-000000000046}', 0, 8, 4)


def main():
    input = r'D:\test\LC.docx'
    output = r'D:\test\联创UWB定位系统操作手册.pdf'
    GenerateSupport()
    rc = doc2pdf(input, output)
    if rc:
        print('转换成功')
    else:
        print('转换失败')


if __name__ == '__main__':
    main()
