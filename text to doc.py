from docx import Document
import os

# Read the first file to understand its structure
file_path = 'F:\ew\islam'

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


# Function to read the content of a file
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()


# Read the lines from the first file
lines = read_file(file_path)
lines[:20]  # Display the first 20 lines to understand the structure


# Function to clean and format the text
def clean_and_format_text(lines):
    # Concatenate lines to form a single string
    text = ' '.join([line.strip() for line in lines if line.strip()])

    # Add full stops at the end of sentences
    # Note: This is a simple approach; more complex sentence boundary detection could be used for better results
    formatted_text = text.replace('  ', '. ').replace(' .', '.').replace(' ?', '?').replace(' !', '!')

    # Break the text into paragraphs (here, we'll break after every 5 sentences for simplicity)
    sentences = formatted_text.split('. ')
    paragraphs = []
    for i in range(0, len(sentences), 5):
        paragraph = '. '.join(sentences[i:i + 5])
        if paragraph:
            paragraphs.append(paragraph)

    return paragraphs


# Function to save the formatted text as a DOC file
def save_as_doc(formatted_text, output_file_path):
    doc = Document()
    for paragraph in formatted_text:
        doc.add_paragraph(paragraph)
    doc.save(output_file_path)


# Clean and format the text of the first file
formatted_text = clean_and_format_text(lines)

# Generate output file path for the first file
output_file_path_1 = os.path.join(output_dir, 'New Microsoft Word Document.docx')

# Save the formatted text as a DOC file
save_as_doc(formatted_text, output_file_path_1)

# Return the path to the generated DOC file
output_file_path_1
