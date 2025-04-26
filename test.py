import os
from trdg.generators import GeneratorFromStrings
from trdg import handwritten_text_generator

FONTS_PATH = '/home/nitis/Projects/Kaithi/Noto_Sans_Kaithi'
WORD_LIST = ['𑂬𑂹𑂫𑂰𑂐𑂹𑂢𑂱𑂍', '𑂇𑂣𑂩𑂸𑂢𑂰', '𑂮𑂴𑂍𑂹𑂭𑂹𑂧𑂞']

os.makedirs("output_images", exist_ok=True)

generator = GeneratorFromStrings(
    WORD_LIST,
    fonts=[os.path.join(FONTS_PATH, 'NotoSansKaithi-Regular.ttf')],
    word_split=True,
    # is_handwritten=True
)




for i, (img, text) in enumerate(generator):
    if i == len(WORD_LIST):
        print("Reached the end of the word list.")
        break
    
    print(f"Generated image for text: {text}")
    
    safe_text = ''.join(c if c.isalnum() else '_' for c in text)
    img_name = f"output_images/image_{safe_text}.png"
    
    img.save(img_name)
    print(f"Saved {img_name}")
