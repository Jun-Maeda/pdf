import os, tkinter, tkinter.filedialog, tkinter.messagebox
from tkinter import filedialog
from connect import pdf_connect

# ファイル選択ダイアログの表示
root = tkinter.Tk()
# 見た目の設定
# 画面作成
root.geometry('300x200') # 画面サイズの設定
root.title('PDF結合ソフト') # 画面タイトルの設定


# ボタンをクリックした時の処理
def btn_click():
    # ファイルの設定
    fTyp = [("","*.pdf")]

    # 同じディレクトリ内を選択する設定
    iDir = os.path.abspath(os.path.dirname(__file__))


    tkinter.messagebox.showinfo('PDF結合アプリ','最初に結合したいファイルを選択してください。')
    a = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)


    tkinter.messagebox.showinfo('PDF結合アプリ','次に結合したいファイルを選択してください。')
    b = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)


    # pdfを保存するファイルを指定する
    root.filename =  filedialog.asksaveasfilename(initialdir = iDir,title = "PDFを保存する",filetypes =  [("pdfFile","*.pdf")])
    name = root.filename
    print (name)

    pdf_connect(a=a,b=b,name=name)

# ボタンの作成
btn = tkinter.Button(root, text='ボタン', command = btn_click) # ボタンの設定(text=ボタンに表示するテキスト)
btn.place(x=130, y=80) #ボタンを配置する位置の設定



root.mainloop()
