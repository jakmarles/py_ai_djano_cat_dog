
# Basic AI that can detect if there a dog or a cat in the picture uploaded

This program is a Django web application that allows users to upload an image of a dog or a cat, and using the tensorflow trained model to classify the image as either a dog or a cat.

The program starts by importing the necessary libraries such as os, numpy, tensorflow, keras, PIL, and django.

Next, the program loads the previously trained model and sets up the data generator using the dataset path defined in the dataset_path variable.

The user can then access the website and submit an image, the image is then passed to the upload_picture view function in the views.py file of the myapp. This function uses the PIL library to open the image file and resize it to 150x150 pixels. Then it converts the image to grayscale and normalizes it. Then it uses the loaded model to predict whether the image is a dog or a cat.
## Deployment


IN ORDER FOR IT TO WORK YOU WILL NEED PYTHON VERSION 3.10.0

Create Virtual Environment.

```bash
pip install virtualenv
virtualenv -p python3.10.0 env
Activate: .\env\Scripts\activate

```
Install dependencies.

```bash
pip install -r .\requirements.txt

```
Run the application.

```bash
python manage.py runserver
```
Navigate to http://127.0.0.1:8000/upload/

## Authors

- [@jakmarles](https://github.com/jakmarles)


# todo/known bugs - 
If the picture upload aint a cat/dog/couldnt recoginze say so.
if no picture selected and the client click upload an error pop up, need to either disable the button if no pic selected or fix it 
