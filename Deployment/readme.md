# Fruit Classification Model Deployment

## Project Structure
```
fruit-classification/
│-- app.py                # Main Flask application
│--fruit_classifier_model.h5  
│-- static/
│   ├── uploads/          # Folder for uploaded images
│-- templates/
│   ├── index.html        # Webpage template
```

###  Run the Flask App in command prompt

python app.py


The application will be accessible at `http://127.0.0.1:5000/`.

## Using the Application
1. Open the application in a browser.
2. Click the **Choose File** button to upload an image.
3. Click **Upload & Predict** to classify the fruit.
4. The uploaded image and predicted fruit name will be displayed.

## Example Screenshot

![Deployed Screenshot](Deployment/before.png)
![Output Screenshot](Deployment/after.png)

## Issues & Troubleshooting
- Ensure the `static/uploads/` directory exists for image uploads.

