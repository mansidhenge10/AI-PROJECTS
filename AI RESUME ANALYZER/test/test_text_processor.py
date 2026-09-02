import sys
import os

# Add project root to Python path
sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from src.text_processor import preprocess_text


text = """
I am an AI Engineer with experience in Python,
Machine Learning, NLP and Deep Learning.
I developed several AI applications.
"""


tokens = preprocess_text(text)

print("Processed text:")
print(tokens)