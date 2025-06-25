from transformers import pipeline
summarizer = pipeline("summarization",model="facebook/bart-large-cnn")  #summarization pipeline using bart model
def summarize_text(text):
    summary=summarizer(text,max_length=150,min_length=30,do_sample=False)
    return summary[0]['summary_text']