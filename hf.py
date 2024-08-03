# Use a pipeline as a high-level helper
from transformers import pipeline

messages = [
    {"role": "user", "content": "What is a blackhole ?"},
]
pipe = pipeline("text-generation", model="meta-llama/Meta-Llama-3.1-8B-Instruct")
pipe(messages)
