#!/usr/bin/env python3
"""
Nederlandse Overheid Wordcloud Generator
Genereert een mooie wordcloud van alle MD bestanden in scraped_content
"""

import os
import glob
import re
from pathlib import Path
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def download_nltk_data():
    """Download benodigde NLTK data"""
    try:
        nltk.data.find('tokenizers/punkt_tab')
        nltk.data.find('corpora/stopwords')
    except LookupError:
        print("Downloading NLTK data...")
        nltk.download('punkt_tab')
        nltk.download('punkt')
        nltk.download('stopwords')

def get_dutch_stopwords():
    """Krijg Nederlandse stopwoorden en voeg custom stopwoorden toe"""
    try:
        dutch_stopwords = set(stopwords.words('dutch'))
    except:
        # Fallback Nederlandse stopwoorden als NLTK niet werkt
        dutch_stopwords = set([
            'de', 'het', 'een', 'en', 'van', 'te', 'dat', 'die', 'in', 'voor', 'op', 'met', 'als', 'zijn', 'er', 'maar', 'om', 'hebben', 'niet', 'of', 'dan', 'wat', 'we', 'hem', 'zijn', 'worden', 'nu', 'zal', 'zo', 'graag', 'nog', 'mijn', 'geen', 'toen', 'moet', 'wel', 'onder', 'jaar', 'tussen', 'ook', 'door', 'veel', 'zoals', 'twee', 'meer', 'man', 'alleen', 'over', 'laatste', 'groot', 'waar', 'naar', 'binnen', 'hier', 'hoe', 'kon', 'omdat', 'aan', 'bij', 'uit', 'tegen', 'na', 'zeer', 'echter', 'zonder', 'waarom', 'kunnen', 'allemaal', 'maken', 'heeft', 'dus', 'mij', 'zou', 'andere', 'iets', 'komen', 'haar', 'toen', 'tijd', 'mensen', 'hij', 'ze', 'zij', 'ik', 'je', 'jij', 'u', 'wij', 'jullie', 'hun', 'deze', 'dit', 'die', 'dat'
        ])
    
    # Voeg extra custom stopwoorden toe
    custom_stopwords = {
        'wordt', 'worden', 'kunnen', 'moeten', 'zijn', 'hebben', 'dient', 'moet', 'kan', 'zal', 'mag', 'zou', 'waren', 'was', 'ben', 'is', 'zijn', 'geeft', 'geven', 'gegeven', 'maken', 'gemaakt', 'doen', 'gedaan', 'gebruikt', 'gebruiken', 'gebruik', 'zoals', 'bijvoorbeeld', 'indien', 'waarbij', 'waarvan', 'waarin', 'waarmee', 'waardoor', 'wanneer', 'waarom', 'waar', 'wie', 'wat', 'hoe', 'welke', 'welk', 'deze', 'dit', 'die', 'dat', 'een', 'de', 'het', 'en', 'van', 'te', 'voor', 'op', 'met', 'als', 'maar', 'om', 'niet', 'of', 'dan', 'we', 'hem', 'nu', 'zo', 'nog', 'mijn', 'geen', 'toen', 'wel', 'onder', 'jaar', 'tussen', 'ook', 'door', 'veel', 'twee', 'meer', 'man', 'alleen', 'over', 'laatste', 'groot', 'naar', 'binnen', 'hier', 'kon', 'omdat', 'aan', 'bij', 'uit', 'tegen', 'na', 'zeer', 'echter', 'zonder', 'allemaal', 'heeft', 'dus', 'mij', 'andere', 'iets', 'komen', 'haar', 'tijd', 'mensen', 'hij', 'ze', 'zij', 'ik', 'je', 'jij', 'u', 'wij', 'jullie', 'hun', 'md', 'https', 'http', 'www', 'nl', 'com', 'org', 'pdf', 'html'
    }
    
    return dutch_stopwords.union(custom_stopwords)

def clean_text(text):
    """Schoon tekst op voor wordcloud"""
    # Verwijder markdown syntax
    text = re.sub(r'##+\s*', '', text)  # Headers
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)  # Links [text](url) -> text
    text = re.sub(r'!\[([^\]]*)\]\([^)]+\)', '', text)  # Images
    text = re.sub(r'`[^`]+`', '', text)  # Inline code
    text = re.sub(r'```[^`]+```', '', text, flags=re.DOTALL)  # Code blocks
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)  # Bold
    text = re.sub(r'\*([^*]+)\*', r'\1', text)  # Italic
    text = re.sub(r'__([^_]+)__', r'\1', text)  # Bold underscore
    text = re.sub(r'_([^_]+)_', r'\1', text)  # Italic underscore
    
    # Verwijder URLs
    text = re.sub(r'https?://[^\s]+', '', text)
    
    # Verwijder email adressen
    text = re.sub(r'\S+@\S+', '', text)
    
    # Verwijder speciale karakters maar behoud Nederlandse karakters
    text = re.sub(r'[^\w\sáàâäéèêëíìîïóòôöúùûüçñ]', ' ', text, flags=re.UNICODE)
    
    # Verwijder extra whitespace
    text = re.sub(r'\s+', ' ', text)
    
    return text.strip()

def read_md_files(directory):
    """Lees alle MD bestanden uit directory"""
    md_files = glob.glob(os.path.join(directory, "*.md"))
    all_text = ""
    
    print(f"Gevonden {len(md_files)} MD bestanden")
    
    for file_path in md_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                all_text += " " + content
                print(f"Gelezen: {os.path.basename(file_path)}")
        except Exception as e:
            print(f"Fout bij lezen {file_path}: {e}")
    
    return all_text

def generate_wordcloud(text, output_path="nederlandse_overheid_wordcloud.png"):
    """Genereer wordcloud met Nederlandse overheid stijl"""
    
    # Definieer kleuren gebaseerd op gegeven hex codes
    colors = ['#0E0076', '#5EA0F7', '#0D0D0D', '#E9EDF2']
    
    def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
        """Custom kleur functie"""
        color_idx = hash(word) % len(colors)
        return colors[color_idx]
    
    # Zoek naar Aharoni font in project directory
    font_candidates = [
        "aharoni.ttf",
        "ahronbd.ttf", 
        "Aharoni.ttf",
        "AHARONI.TTF",
        "fonts/aharoni.ttf",
        "fonts/ahronbd.ttf"
    ]
    
    font_path = None
    for font_file in font_candidates:
        if os.path.exists(font_file):
            font_path = font_file
            print(f"Aharoni font gevonden: {font_path}")
            break
    
    if not font_path:
        print("Aharoni font niet gevonden, gebruik standaard font")
    
    # WordCloud configuratie
    wordcloud = WordCloud(
        width=1920,
        height=1080,
        background_color='white',
        max_words=200,
        font_path=font_path,
        color_func=color_func,
        relative_scaling=0.5,
        random_state=42,
        collocations=False,
        min_font_size=10
    ).generate(text)
    
    # Creëer figuur en plot
    plt.figure(figsize=(20, 10))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Nederlandse Overheid AI & Algoritme Wordcloud', 
              fontsize=24, fontweight='bold', color='#0E0076', pad=20)
    
    # Sla op met hoge resolutie
    plt.savefig(output_path, dpi=300, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    plt.show()
    
    print(f"Wordcloud opgeslagen als: {output_path}")

def main():
    """Hoofdfunctie"""
    print("Nederlandse Overheid Wordcloud Generator")
    print("=" * 50)
    
    # Download NLTK data indien nodig
    download_nltk_data()
    
    # Pad naar scraped content
    content_dir = "1. Datasets/Scrapen/scraped_content/content"
    
    if not os.path.exists(content_dir):
        print(f"Directory niet gevonden: {content_dir}")
        return
    
    # Lees alle MD bestanden
    print(f"Lezen van MD bestanden uit: {content_dir}")
    raw_text = read_md_files(content_dir)
    
    if not raw_text.strip():
        print("Geen tekst gevonden in MD bestanden")
        return
    
    print(f"Totaal aantal karakters: {len(raw_text)}")
    
    # Schoon tekst op
    print("Tekst opschonen...")
    clean_content = clean_text(raw_text)
    
    # Verwijder stopwoorden
    print("Nederlandse stopwoorden verwijderen...")
    dutch_stopwords = get_dutch_stopwords()
    
    # Tokenize en filter
    words = word_tokenize(clean_content.lower())
    filtered_words = [word for word in words if word not in dutch_stopwords and len(word) > 2]
    
    print(f"Aantal woorden na filtering: {len(filtered_words)}")
    
    # Toon meest voorkomende woorden
    word_freq = Counter(filtered_words)
    print("\nTop 20 meest voorkomende woorden:")
    for word, count in word_freq.most_common(20):
        print(f"  {word}: {count}")
    
    # Genereer wordcloud
    print("\nWordcloud genereren...")
    final_text = ' '.join(filtered_words)
    generate_wordcloud(final_text)
    
    print("Klaar!")

if __name__ == "__main__":
    main()