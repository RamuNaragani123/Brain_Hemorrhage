<<<<<<< HEAD
# Brain Hemorrhage Detection using Deep Learning

A Django web application that accepts a brain scan image and uses a pre-trained TensorFlow/Keras model to predict one of two labels: `Hemorrhogic` or `Non Hemorrhogic`.

> **Important:** This is an educational project, not a medical device. Its predictions are not a diagnosis and must not be used to make medical decisions.

## Project structure

```text
.
├── manage.py
├── keras_model.h5
├── requirements.txt
├── project/
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── trainmodel.py
├── templates/
└── static/
```

## Requirements

- Python 3.8–3.11 (TensorFlow 2.13.1 compatible versions)
- Git (for GitHub upload)
- A virtual environment is recommended

## Run locally (Windows / VS Code)

Open the terminal in the folder containing `manage.py`.

1. Create a virtual environment:

   ```powershell
   py -3.10 -m venv .venv
   ```

   If Python 3.10 is not installed, install a TensorFlow-compatible Python version first.

2. Activate it:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   If PowerShell blocks activation, run this in the current terminal only:

   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   .\.venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```powershell
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. Create the local database tables:

   ```powershell
   python manage.py migrate
   ```

5. Check the Django project:

   ```powershell
   python manage.py check
   ```

6. Start the development server:

   ```powershell
   python manage.py runserver
   ```

7. Open http://127.0.0.1:8000/ in your browser and use **Features** to upload a PNG or JPG image.

The first startup can take some time while TensorFlow loads the model.

## Push to GitHub

Create a new **empty** repository on GitHub (do not add a README or license if you already have this one), then run these commands in the project folder:

```powershell
git init
git add .
git status
git commit -m "Initial commit: brain hemorrhage detection app"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

Replace the URL with your repository's actual HTTPS URL. Sign in through the Git credential prompt if requested. Never put your GitHub password or access token into source code.

## Notes

- The trained `keras_model.h5` is included and is small enough for a normal GitHub repository.
- Dataset images, training notebooks, local database, and extra training experiments are excluded from Git by `.gitignore`.
- If the model predicts unexpected labels, verify the model's original training preprocessing and class order. The code currently follows the labels file included with the original project: class 0 = `Hemorrhogic`, class 1 = `Non Hemorrhogic`.
- For deployment, replace the development settings and secret key, configure allowed hosts, and use a production server.
=======
# Brain_Hemorrhage
>>>>>>> b8668525eaa23191054402350f85ef881c0a474a
