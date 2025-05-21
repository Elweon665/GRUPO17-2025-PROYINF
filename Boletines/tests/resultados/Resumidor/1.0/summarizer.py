from transformers import pipeline

resumidor = pipeline("summarization", model="facebook/bart-large-cnn")

def chunkGenerator(texto, max_tokens=3000):
    tokens = texto.split()
    chunks = []
    chunk_actual = ""
    count = 0
    
    for palabra in tokens:
        if count <= max_tokens:
            chunk_actual += " " + palabra if chunk_actual else palabra
            count += 1
        else:
            chunks.append(chunk_actual)
            chunk_actual = ""
            count = 0
    
    if chunk_actual:
        chunks.append(chunk_actual)
    
    return chunks       

def generarResumen(texto):
    chunks = chunkGenerator(texto)
    print(chunks)
    res = resumidor(chunks[0], max_length=100, min_length=1, do_sample=False)
    print(res)
    output = [resumidor(chunk, max_length=len(texto.split()), min_length=int(len(chunk.split())/2), do_sample=False)[0]['summary_text'] for chunk in chunks]
    #output = [resumidor(chunk, max_length=min(130, len(chunk.split())), min_length=int(len(chunk.split()) * 0.3), do_sample=False)[0]['summary_text'] for chunk in chunks]
    return " ".join(output)