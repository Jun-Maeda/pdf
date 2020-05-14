import PyPDF2

# PyPDF2を読み込む
def pdf_connect(a,b,name):
    merger = PyPDF2.PdfFileMerger()

    # 結合したいフィアルを先ほど作成した変数に追加していく
    merger.append(a)
    merger.append(b)

    # 作成するファイル名を出力
    merger.write("{}".format(name))
    merger.close
