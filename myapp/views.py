from django.shortcuts import render
from PIL import Image
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model('D:\py_ai\model') # Loading the model 

def upload_picture(request):
    if request.method == 'POST':
        # Handle the image upload
        image = request.FILES['image']
        img = Image.open(image)
        img = img.resize((150,150))
        img = img.convert("L") # convert to grayscale
        img = np.array(img)
        img = img/255 # normalizing
        img = np.expand_dims(img, axis=0)

        # Make a prediction
        prediction = model.predict(img)

        # Determine if the image is a dog or a cat
        if prediction[0] > 0.5:
            message = "It's a dog!"
        else:
            message = "It's a cat!"

        # Render the template
        return render(request, 'classification.html', {'message': message})
    else:
        # Render the template for the form
        return render(request, 'upload.html')