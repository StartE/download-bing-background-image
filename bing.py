import requests
import re
import os.path

save_dir ="images"
proxy= {} # proxy = {'http':'xxx.xx.com:port_num'}

page_url = 'https://www.bing.com'
response_code = {'OK':200}


class DownloadBingImage():

    def __init__(self,save_dir,page_url = page_url,proxy = {}):
        self.save_dir = save_dir
        self.page_url = page_url
        self.proxy = proxy

    
    def get_bing_image_url(self):
        load_page = requests.get(self.page_url,proxies = self.proxy)
        if(load_page.status_code == response_code['OK']):
            pattern = r"url:[.,/_:\s\-\"\'a-zA-Z0-9]+bgDiv"
            search_img_url =re.search(pattern,load_page.text)
            if search_img_url!= None:
                url = search_img_url.group()
                url = url.split('"')[1]
                url = page_url + url
                return url
            else:
                print('Could Not Get the Image URL')
                return
        else:
            print("Network Error, Response Code is {}".format(load_page.status_code))
            return
    def save_bing_image(self,image_url,file_name = None):
        load_img = requests.get(image_url,proxies = self.proxy)
        if file_name == None:
            file_name = image_url.split('/')[-1]
        save_path = os.path.join(self.save_dir,file_name)

        if(load_img.status_code == response_code['OK']):
            with open(save_path,'wb') as f:
                f.write(load_img.content)
                print('Successfully Download the Beautiful Image!')
        else:
            print("Network Error, Response Code is {}".format(load_img.status_code))

def main():

    bing = DownloadBingImage(save_dir)
    image_url = bing.get_bing_image_url()
    if image_url:
        bing.save_bing_image(image_url)
    else:
        print('#=======I will check the url later please wait for patience===========')

if __name__ == "__main__":
    main()
