from webview import Webview
import tkinter

def main():
    mainWindow = tkinter.Tk()

    mainWindow.title('网页监控器')
    mainWindow.resizable(0,0)
    mainWindow.geometry('800x600')

    landpageEntry = tkinter.Entry(exportselection = 0, width = 44, font = ('Arial', 20))
    landpageEntry.place(x = 63, y = 90)

    mainText = tkinter.Text(width = 17, height = 1, font = ('Arial', 50))
    mainText.place(x = 80, y = 300)

    def cilck():
        landurl = landpageEntry.get()
        path = 'C:/Users/庄依林/OneDrive/桌面/Code/class/webview/'

        web = Webview(url = landurl, oripage = path + 'oripage', file_dir = path)

        if not web.web_diff():
            mainText.delete(0.0, tkinter.END)
            mainText.insert(tkinter.INSERT,'        WARNING!')
        else:
            mainText.delete(0.0, tkinter.END)
            mainText.insert(tkinter.INSERT, '   nothing happened')

    btn = tkinter.Button(text = 'DO IT !', width = 10, height = 2, font = ('黑体', 30), command = cilck)
    btn.place(x = 325, y = 480)

    mainWindow.mainloop()

if __name__ == '__main__':
    main()