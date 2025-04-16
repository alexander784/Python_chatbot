## Python Chatbot

<p>This project is a web-based chatbot application built using Django and the ChatterBot library. It provides a user-friendly interface for interacting with a conversational AI powered by pre-trained English language corpora. The chatbot processes user inputs via HTTP requests and responds dynamically using a best-match logic adapter.</p>

## Features
* **Web Interface:** A clean, responsive front-end for seamless user interaction.
* COnversational AI: Leverages ChatterBot for natural language processing and response generation.
* RESTful API: Handles user messages via GET requests and returns JSON responses.
* Customizable Responses: Configurable default response for unrecognized inputs.
* **Extensible Training:** Supports additional training with custom corpora.

## Prerequisites
* Python 3.10.12
* Django
* ChatterBot==1.0.5
* PyYAML (included with ChatterBot)

## Installation**
1. **Clone the Repo:**
   ```bash
   https://github.com/alexander784/Python_chatbot.git
   cd Python_chatbot
2. **Create a virtual env**
   ```python -m venv venv
      source venv/bin/activate
3. **INstall dependecies**
    ```bash 
    pip install chatterbot==1.0.5

4. **Apply migrations:**
   ```bash 
   python manage.py migrate


## Usage
1. **Start Django development server**
   ```bash 
   python3 manage.py runserver

2. Open your browser and navigate to `http://127.0.0.1:8000` to access the chatbot interface.

3. Type messages in the provided input field to interact with the chatbot.

**Front-End Template `(chatbotapp/templates/chatbotapp/index.html)`**

<p>

A basic HTML template with JavaScript for handling user input and displaying responses is required. Refer to the project repository for the complete template.</p>

## Configurations
**Login Adapter:** Uses BestMatch with a 0.9 similarity threshold for high-confidence responses.

**Default Responses**:Returns "Sorry am not conversate with that" for low-confidence matches.


**Training Data:** Pre-trained with chatterbot.corpus.english. Extend training by modifying the trainer.train() method.

**Django Settings** Ensure chatbotapp is added to INSTALLED_APPS in settings.py.


## Contributing
**Contributions are always welcome! To contribute:**

* Fork the repository.
* Create a new branch `(git checkout -b feature-branch).`
* Commit your changes `(git commit -m "Add feature")`.
* Push to the branch `(git push origin feature-branch)`.
* Open a Pull Request.

## License
<p>This project is licensed under the MIT License. See the LICENSE file for details.</p>

## Acknowledgements
* Django for the web framework.
* ChatterBot for the conversational AI framework.



 






