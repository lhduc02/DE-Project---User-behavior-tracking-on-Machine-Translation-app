from transformers import MarianMTModel, MarianTokenizer

def machine_translation(language_source, language_destination, input_content):
    # Mapping language names to MarianMT model format
    lang_code_mapping = {
        "English": "en", "French": "fr", "German": "de", "Spanish": "es",
        "Italian": "it", "Portuguese": "pt", "Dutch": "nl", "Russian": "ru"
    }
    
    src_lang = lang_code_mapping.get(language_source, "en")
    tgt_lang = lang_code_mapping.get(language_destination, "fr")
    model_name = f"Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}"
    
    # Load model and tokenizer
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    
    # Tokenize input text
    input_tokens = tokenizer(input_content, return_tensors="pt", padding=True, truncation=True)
    
    # Generate translation
    translated_tokens = model.generate(**input_tokens)
    output_content = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
    
    return output_content

# # Example usage
# language_source = "English"
# language_destination = "Russian"
# input_content = """
# Apache Spark is an open-source unified analytics engine for large-scale data processing. Spark provides an interface for programming clusters with implicit data parallelism and fault tolerance. Originally developed at the University of California, Berkeley's AMPLab starting in 2009, in 2013, the Spark codebase was donated to the Apache Software Foundation, which has maintained it since.
# Apache Spark has its architectural foundation in the resilient distributed dataset (RDD), a read-only multiset of data items distributed over a cluster of machines, that is maintained in a fault-tolerant way. The Dataframe API was released as an abstraction on top of the RDD, followed by the Dataset API. In Spark 1.x, the RDD was the primary application programming interface (API), but as of Spark 2.x use of the Dataset API is encouraged even though the RDD API is not deprecated. The RDD technology still underlies the Dataset API
# """
# output_content = machine_translation(language_source, language_destination, input_content)
# print("Translated Text:", output_content)
