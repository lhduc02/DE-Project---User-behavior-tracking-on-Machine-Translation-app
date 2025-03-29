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

# Example usage
language_source = "English"
language_destination = "French"
input_content = "hello world this is a test"
output_content = machine_translation(language_source, language_destination, input_content)
print("Translated Text:", output_content)
