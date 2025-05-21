from transformers import pipeline, AutoTokenizer

resumidor = pipeline("summarization", model="facebook/bart-large-cnn")
tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")

def chunkGenerator(texto, max_tokens=800):
    texto = texto.split()
    texto = " ".join(texto)
    tokens = tokenizer.encode(texto, truncation=False)
    chunks = []
    
    for i in range(0, len(tokens), max_tokens):
        chunk_tokens = tokens[i:i + max_tokens]
        if chunk_tokens:
            chunk_text = tokenizer.decode(chunk_tokens, skip_special_tokens=True, clean_up_tokenization_spaces=True)
            chunks.append(chunk_text)

    return chunks      

def generarResumen(texto):
    chunks = chunkGenerator(texto)
    output = [resumidor(chunk, max_length=len(chunk.split()), min_length=int(len(chunk.split())/2), do_sample=False)[0]['summary_text'] for chunk in chunks]
    return " ".join(output)