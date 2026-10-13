import webbrowser

def check(func):
    def wrapper(url):
        if '.' in url and '//' in url:
            pass
        if 'http:' in url or 'https:' in url:
            func(url)
        else:
            print('Неверный формат URL')
    return wrapper    

@check
def open_url(url):
    webbrowser.open(url)

open_url('https://youtube.com')
