# 🌐 AI Language Translator

An AI-powered language translation web application built with **Python and Streamlit** as part of the **CodeAlpha Artificial Intelligence Internship**.

The application allows users to enter text, select a source and target language, translate the text using an online translation service, listen to the translated result, copy the translation, swap languages, and view recent translation history.

---

## 📌 Project Overview

The AI Language Translator provides a simple and user-friendly interface for translating text between multiple languages.

The project was developed to demonstrate:

* Python programming
* Streamlit web application development
* Translation service integration
* Natural language processing through an external translation service
* Text-to-speech functionality
* Session-state management
* Error handling
* User interface design

This project fulfills the core requirements of **CodeAlpha Task 1: Language Translation Tool**.

---

## ✨ Features

### Core Features

* 🌐 Translate text between multiple languages
* 📝 Text input area for entering or pasting content
* 🔤 Source language selection
* 🌍 Target language selection
* 🔄 One-click translation
* 🔄 Swap source and target languages
* 📋 Copy translated text
* 🔊 Convert translated text to speech
* 📚 Store and display recent translations
* ⚠️ Basic error handling
* 📱 Clean and simple Streamlit interface

---

## 🌍 Supported Languages

The current version supports:

| Language | Code    |
| -------- | ------- |
| English  | `en`    |
| Hindi    | `hi`    |
| Spanish  | `es`    |
| French   | `fr`    |
| German   | `de`    |
| Italian  | `it`    |
| Japanese | `ja`    |
| Korean   | `ko`    |
| Chinese  | `zh-CN` |

---

## 🛠️ Technologies Used

* **Python**
* **Streamlit** — Web application interface
* **deep-translator** — Translation service integration
* **Google Translate** — Translation service accessed through `deep-translator`
* **gTTS (Google Text-to-Speech)** — Text-to-speech functionality
* **BytesIO** — Handling generated audio data

---

## 📂 Project Structure

```text
CodeAlpha_LanguageTranslationTool/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── venv/
```

> `venv/` is a local Python virtual environment and should not be uploaded to GitHub.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project directory

```bash
cd CodeAlpha_LanguageTranslationTool
```

### 3. Create a virtual environment

Windows:

```bash
python -m venv venv
```

### 4. Activate the virtual environment

PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

Command Prompt:

```cmd
venv\Scripts\activate
```

### 5. Install the required dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python -m streamlit run app.py
```

The application will normally be available at:

```text
http://localhost:8501
```

---

## 🖥️ How to Use

### Step 1 — Select Languages

Choose the language of the input text using **Source Language**.

Choose the desired output language using **Target Language**.

### Step 2 — Enter Text

Enter or paste the text you want to translate into the text box.

### Step 3 — Translate

Click:

```text
🔄 Translate
```

The application sends the text to the translation service and displays the translated result.

### Step 4 — Copy Translation

Use the **Copy Translation** button to copy the translated text.

### Step 5 — Listen to Translation

Click:

```text
🔊 Generate Speech
```

The application generates an audio version of the translated text.

### Step 6 — Swap Languages

Click the:

```text
🔄
```

button between the language selectors to swap the source and target languages.

### Step 7 — View History

The application maintains a recent translation history during the current session.

---

## 🧠 How It Works

The application follows this basic flow:

```text
User Input
    ↓
Streamlit Interface
    ↓
Source & Target Language Selection
    ↓
Translation Request
    ↓
Translation Service
    ↓
Translated Text
    ↓
Display Result
    ↓
Copy / Text-to-Speech / History
```

The translation functionality is implemented using `deep-translator` and `GoogleTranslator`.

Example:

```python
translator = GoogleTranslator(
    source=languages[source_language]["code"],
    target=languages[target_language]["code"]
)

translated_text = translator.translate(text)
```

The translated result is then stored using Streamlit session state and displayed in the interface.

---

## 🔊 Text-to-Speech

The project uses **gTTS (Google Text-to-Speech)** to generate speech from the translated text.

The generated audio is stored temporarily in memory using `BytesIO` and then played through Streamlit's audio player.

---

## 📚 Translation History

The application stores recent translations in Streamlit's session state.

Each history entry contains:

* Source language
* Target language
* Original text
* Translated text

The application keeps the most recent five translations.

---

## ⚠️ Error Handling

The application includes basic error handling for situations such as:

* Empty input
* Selecting the same source and target language
* Translation service failure
* Internet connection problems
* Text-to-speech generation failure

---

## 📋 Internship Task

This project was developed for:

**CodeAlpha — Artificial Intelligence Internship**

### Task 1: Language Translation Tool

The project implements the requested translation tool functionality, including:

* User text input
* Source language selection
* Target language selection
* Translation processing
* Displaying translated text

Optional functionality has also been added, including:

* Copy translation
* Text-to-speech

---

## 🚀 Future Improvements

Possible improvements for future versions include:

* Automatic source-language detection
* Support for additional languages
* More advanced UI customization
* Translation API authentication
* Translation history persistence using a database
* Voice input
* Improved accessibility
* Dark/light theme customization
* Deployment to a public cloud platform

---

## 👨‍💻 Author

**Shlok**

Developed as part of the **CodeAlpha Artificial Intelligence Internship**.

---

## 📄 License

This project was created for educational and internship purposes.
