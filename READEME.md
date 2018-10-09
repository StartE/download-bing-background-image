# Download Bing Background Image 

A simple and elegant way to download beautiful image of [bing](https://cn.bing.com)

## Requirements
* pip install [requests](http://docs.python-requests.org/en/master/)

## Example
* set the *save_dir* of images
```py
import bing
# modify it with your requirement
save_dir ="images"

download_bing = bing.DownloadBingImage(save_dir)
image_url = download_bing.get_bing_image_url()
if image_url:
    download_bing.save_bing_image(image_url)
```
* you can also set the proxy if necessary
