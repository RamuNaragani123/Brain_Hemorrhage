from io import BytesIO

import numpy as np
from PIL import Image, UnidentifiedImageError
from django.shortcuts import render
from .trainmodel import model


def home(request):
    return render(request, "index.html")


def abstract(request):
    return render(request, "abstract.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "about.html")


def performance(request):
    return render(request, "gallery.html")


def result(request):
    return render(request, "result.html")


def upload(request):
    context = {}
    if request.method == "POST":
        uploaded_file = request.FILES.get("myfile")
        if not uploaded_file:
            context["error"] = "Please choose a brain scan image first."
            return render(request, "upload.html", context)

        allowed_types = {"image/jpeg", "image/png", "image/jpg"}
        if uploaded_file.content_type not in allowed_types:
            context["error"] = "Please upload a PNG or JPG image."
            return render(request, "upload.html", context)

        if uploaded_file.size > 10 * 1024 * 1024:
            context["error"] = "Image size must be 10 MB or less."
            return render(request, "upload.html", context)

        try:
            image = Image.open(BytesIO(uploaded_file.read())).convert("RGB")
            image = image.resize((224, 224))
            image_array = np.asarray(image, dtype=np.float32) / 255.0
            image_array = np.expand_dims(image_array, axis=0)

            predictions = model.predict(image_array, verbose=0)
            predicted_class = int(np.argmax(predictions, axis=1)[0])
            class_names = ["Hemorrhogic", "Non Hemorrhogic"]
            context["predicted_class"] = class_names[predicted_class]
        except (UnidentifiedImageError, OSError, ValueError, IndexError):
            context["error"] = "The uploaded file could not be read as a valid image."

    return render(request, "upload.html", context)
