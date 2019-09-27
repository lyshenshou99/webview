from webview import Webview
import time

def main():
    delay = eval(input('please input the delay time:'))
    url = input('please input the url:')
    path = input('please input the path:')
    num = eval(input('please input the round:'))

    web = Webview(url = url, oripage = path + "oriweb", file_dir = path)
    web.save_file0()

    for eachround in range(num):
        print("It's the {} times,".format(eachround), end = '')
        
        if web.web_diff:
            print('nothing happened')
        else:
            print('warning!')

        time.sleep(delay)

if __name__ == '__main__':
    main()