import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
from io import BytesIO
import streamlit.components.v1 as components





st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌐",
    layout="centered"
)





languages = {
    "English": {
        "code": "en",
        "tts": "en"
    },
    "Hindi": {
        "code": "hi",
        "tts": "hi"
    },
    "Spanish": {
        "code": "es",
        "tts": "es"
    },
    "French": {
        "code": "fr",
        "tts": "fr"
    },
    "German": {
        "code": "de",
        "tts": "de"
    },
    "Italian": {
        "code": "it",
        "tts": "it"
    },
    "Japanese": {
        "code": "ja",
        "tts": "ja"
    },
    "Korean": {
        "code": "ko",
        "tts": "ko"
    },
    "Chinese": {
        "code": "zh-CN",
        "tts": "zh-CN"
    }
}





if "source_language" not in st.session_state:
    st.session_state.source_language = "English"

if "target_language" not in st.session_state:
    st.session_state.target_language = "Hindi"

if "translated_text" not in st.session_state:
    st.session_state.translated_text = ""

if "translation_history" not in st.session_state:
    st.session_state.translation_history = []




st.title("🌐 AI Language Translator")

st.write(
    "Translate text between multiple languages using an online "
    "translation service."
)

st.divider()





language_names = list(languages.keys())

col1, col2, col3 = st.columns([5, 1, 5])

with col1:
    source_language = st.selectbox(
        "Source Language",
        language_names,
        index=language_names.index(
            st.session_state.source_language
        )
    )

with col2:
    st.write("")
    st.write("")

    if st.button("🔄", help="Swap languages"):

        st.session_state.source_language, st.session_state.target_language = (
            st.session_state.target_language,
            st.session_state.source_language
        )

        st.session_state.translated_text = ""

        st.rerun()

with col3:
    target_language = st.selectbox(
        "Target Language",
        language_names,
        index=language_names.index(
            st.session_state.target_language
        )
    )

# Save the selections
st.session_state.source_language = source_language
st.session_state.target_language = target_language

st.session_state.source_language = source_language
st.session_state.target_language = target_language




text = st.text_area(
    "Enter text to translate",
    height=180,
    placeholder="Type or paste your text here..."
)




if st.button(
    "🔄 Translate",
    use_container_width=True,
    type="primary"
):

    if not text.strip():

        st.warning("Please enter some text first.")

    elif source_language == target_language:

        st.info(
            "Source and target languages are the same."
        )

    else:

        try:

            translator = GoogleTranslator(
                source=languages[source_language]["code"],
                target=languages[target_language]["code"]
            )

            translated_text = translator.translate(text)

            st.session_state.translated_text = translated_text

            # Save translation to history
            st.session_state.translation_history.insert(
                0,
                {
                    "source": source_language,
                    "target": target_language,
                    "original": text,
                    "translation": translated_text
                }
            )

            # Keep only the last 5 translations
            st.session_state.translation_history = (
                st.session_state.translation_history[:5]
            )

        except Exception:

            st.error(
                "Translation failed. Please check your "
                "internet connection and try again."
            )





if st.session_state.translated_text:

    st.divider()

    st.subheader("📝 Translation")

    translated_text = st.session_state.translated_text

    st.text_area(
        "Translated text",
        value=translated_text,
        height=150,
        disabled=True
    )


 

    st.markdown("### 📋 Copy Translation")

    escaped_text = (
        translated_text
        .replace("\\", "\\\\")
        .replace("`", "\\`")
        .replace("${", "\\${")
    )

    components.html(
        f"""
        <button
            onclick="navigator.clipboard.writeText(`{escaped_text}`)"
            style="
                width:100%;
                padding:10px;
                border-radius:8px;
                border:1px solid #555;
                background:#262730;
                color:white;
                cursor:pointer;
                font-size:16px;
            "
        >
            📋 Copy Translation
        </button>
        """,
        height=50
    )


 

    st.markdown("### 🔊 Listen")

    if st.button(
        "🔊 Generate Speech",
        use_container_width=True
    ):

        try:

            speech = gTTS(
                text=translated_text,
                lang=languages[target_language]["tts"]
            )

            audio_data = BytesIO()

            speech.write_to_fp(audio_data)

            audio_data.seek(0)

            st.audio(
                audio_data,
                format="audio/mp3"
            )

        except Exception:

            st.error(
                "Text-to-speech could not be generated."
            )



 

if st.session_state.translation_history:

    st.divider()

    st.subheader("📚 Recent Translations")

    for item in st.session_state.translation_history:

        with st.expander(
            f"{item['source']} → {item['target']}"
        ):

            st.write("**Original:**")
            st.write(item["original"])

            st.write("**Translation:**")
            st.write(item["translation"])