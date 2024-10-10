import nltk
from nltk.tokenize import word_tokenize
import streamlit as st

# Download the punkt tokenizer if not already downloaded
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt_tab')

# Castle Swimmer knowledge base
# Expanded Castle Swimmer knowledge base
castle_swimmer_knowledge = {
    "what is castle swimmer about": "Castle Swimmer is a webtoon about a group of young adults living in a mystical world where they navigate love, friendship, and their destinies. The story explores themes of sacrifice, loyalty, and the power of choice.",
    
    "who are the main characters": (
        "The main characters are:\n"
        "- **Roin**: A brave and determined protagonist who seeks to fulfill the prophecy.\n"
        "- **Giom**: Roin's loyal friend, who often provides comic relief while supporting the main quest.\n"
        "- **Kite**: A mysterious figure with a troubled past, deeply connected to the prophecy."
    ),
    
    "what is the prophecy": (
        "The prophecy revolves around a chosen one who will save their world from destruction. "
        "It speaks of trials that the chosen must face and the alliances they must forge to succeed."
    ),
    
    "what happens in chapters 83-89": (
        "Chapters 83-89 unveil new developments in the prophecy and character relationships. "
        "Roin discovers hidden truths about his heritage, leading to unexpected challenges and alliances. "
        "The dynamics between Roin, Giom, and Kite evolve, revealing deeper emotional connections."
    ),
    
    "what are the main themes of castle swimmer": (
        "The webtoon explores several themes, including:\n"
        "- **Identity**: Characters struggle with their past and seek to understand their true selves.\n"
        "- **Friendship**: The importance of bonds between friends is highlighted throughout the journey.\n"
        "- **Courage**: Characters face their fears and take bold actions to achieve their goals.\n"
        "- **Love**: Romantic relationships develop amidst the chaos, adding depth to character motivations."
    ),
    
    "who is the author": "Castle Swimmer is created by the talented artist and writer, who brings a unique visual style and storytelling approach to the webtoon.",
    
    "what is the art style of castle swimmer": (
        "The art style of Castle Swimmer is characterized by vibrant colors and expressive character designs. "
        "The backgrounds are richly detailed, immersing readers in the mystical world."
    ),
    
    "how many chapters are there": "As of now, Castle Swimmer has over 100 chapters, with new updates being released regularly.",
    
    "who are the antagonists in the story": (
        "The story features several antagonists, including:\n"
        "- **The Dark Sorcerer**: A powerful figure seeking to harness the prophecy for his own gain.\n"
        "- **The Rival Clan**: An opposing faction that challenges Roin and his friends at every turn."
    ),
    
    "what makes castle swimmer unique": (
        "Castle Swimmer stands out due to its combination of engaging storytelling, well-developed characters, "
        "and the seamless blend of romance, action, and fantasy elements."
    ),
    
    "where can I read castle swimmer": "You can read Castle Swimmer on popular webtoon platforms like Webtoon and Tapas."
}

# Basic chatbot function
def chatbot(input_text):
    input_text = input_text.lower()  # Convert to lowercase for matching

    # Check for specific phrases
    if "castle swimmer" in input_text and "about" in input_text:
        return castle_swimmer_knowledge["what is castle swimmer about"]
    elif "main characters" in input_text:
        return castle_swimmer_knowledge["who are the main characters"]
    elif "prophecy" in input_text:
        return castle_swimmer_knowledge["what is the prophecy"]
    elif "chapters 83-89" in input_text:
        return castle_swimmer_knowledge["what happens in chapters 83-89"]
    
    return "Sorry, I'm not sure about that."

# Streamlit app
def main():
    st.title("Castle Swimmer Chatbot")
    user_input = st.text_input("Ask me anything about Castle Swimmer:")
    
    if user_input:
        response = chatbot(user_input)
        st.write("Chatbot:", response)

if __name__ == "__main__":
    main()
