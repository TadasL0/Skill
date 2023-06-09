from transformers import pipeline

# Load the pre-trained summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Get user input
text = input("What's on your mind?: ")

# Perform text summarization
summary = summarizer(text, max_length=100, min_length=30,
                     do_sample=False)[0]["summary_text"]

# Print the summary
print("Output:")
print(summary)
