# InstaPick

Let's say that you have a bunch of images in a folder, and some of then come from *instagram*. For example, the "camera uploads" folder in dropbox, if you configure it properly, will contain all the images you take with your mobile phone camera. Once you take the photo, it is synced to this folder.

Normally, when we upload an image to *instagram* it is down-sized. If later on, you want to download this image, you will lose the original size. Therefore, it makes sense to keep your original *instagram* image, which, in fact, it is saved to your "camera uploads" folder via dropbox, or whichever other syncing software you have.

If you want to pick the *instagram* images manually, you have to traverse all the images on the folder (and this can be very time-consuming). Therefore, **i have developed this brief python tool, which lets you to automatically pick the *instagram* images from one folder and copy to another folder**, based on the *EXIF information* of the image. Thus, you will have all your *instagram* images in one destination folder.

## Installation & Usage

~~~bash
# clone repo
$ pipenv install
# edit .env file with the corresponding values
$ pipenv run python main.py
~~~
