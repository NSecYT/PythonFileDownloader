import requests

def download(url):
    get_response = requests.get(url)
    file_name = url.split('/')[-1]
    with open(file_name,'wb')as out_file:
        out_file.write(get_response.content)


download('https://az764295.vo.msecnd.net/stable/ea3859d4ba2f3e577a159bc91e3074c5d85c0523/VSCodeUserSetup-x64-1.52.1.exe')
