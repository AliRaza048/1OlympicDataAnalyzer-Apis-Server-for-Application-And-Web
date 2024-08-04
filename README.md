# Server/Apis for Olympic Data Analyzer Application & Web
  This repository contains the backend API for the Olympic Data Analyzer project, developed using Python and Django. 
  The API provides endpoints to fetch and analyze Olympic data.

# Ensure you have the following installed on your system:
  - Python
  - pip
    
# Installation
  1. Clone the repository: git clone cd
  2. Install the required Python packages: pip install -r requirements.txt
  3. Running the Server: python manage.py runserver #OR python manage.py runserver 8000
     
# Exposing the Local Server with ngrok
  1. Download the ngrok zip file from the official ngrok website and sign up. https://ngrok.com/download
  2. Extract the zip file to a directory of your choice.
  3. Add the extracted path to your environment variables.
  4. Set Ngrok Authentication Token: You will find the authentication token on the Ngrok dashboard. Copy that token.
  5. To set the Ngrok authentication token globally in the Command Prompt, run this command: ngrok authtoken (your-authentication-token). Replace with your actual authentication token copy.
  6. Run the following command globally in the command prompt: ngrok http 8000

# Integrating with the Expo Project
  1. Copy the generated ngrok address (ex: https://0bae-111-68-98-163.ngrok-free.app).
  2. Update the serverUrl in the urls.js file located in the apis folder of Expo project:
