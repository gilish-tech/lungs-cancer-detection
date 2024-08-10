import gradio as gr
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model

# Load your trained model
model = load_model('./drive/MyDrive/model_3.h5')

# Define the image processing function (grayscale conversion and normalization)
def preprocess_image(image):
    # Resize the image to 224x224
    image = tf.image.resize(image, (224, 224))
    # Convert to grayscale
    image = tf.image.rgb_to_grayscale(image)
    # Normalize the image
    image = image / 255.0
    # Add a batch dimension (required for prediction)
    image = tf.expand_dims(image, axis=0)
    return image

# Define the prediction function
def predict(image):
    # Preprocess the image
    processed_image = preprocess_image(image)
    # Get the prediction
    prediction = model.predict(processed_image)
    # Return the result
    if prediction[0] > 0.5:
        return "Malignant"
    else:
        return "Benign"

# Define the Gradio interface
interface = gr.Interface(
    fn=predict,  # The function to be called
    inputs=gr.Image(),  # Input type is an image
    outputs="text",  # Output type is text
    title="Lung Cancer Classification",
    description="Upload an image of a lung X-ray to classify it as malignant or benign."
)

# Launch the interface
interface.launch()
