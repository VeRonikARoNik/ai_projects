import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# Reszta kodu...
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def helsinki_translator(user_input):
    tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-pl-en")
    model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-pl-en")

    encoded_pl = tokenizer(user_input, return_tensors="pt")
    output = model.generate(
        **encoded_pl,
        max_length=50,
        num_beams=5,
        no_repeat_ngram_size=2,
        early_stopping=True
    )
    response_str = tokenizer.decode(output[0], skip_special_tokens=True)
    return response_str


def main():
    print("Witamy w aplikacji tłumacz!")
    print("Tłumaczenie z języka polskiego na angielski.")
    print("Wpisz 'exit' aby zakończyć program.\n")
    
    while True:
        user_text = input("Podaj tekst po polsku: ")
        if user_text.lower() == "exit":
            print("Koniec działania aplikacji.")
            break
        
        translation = helsinki_translator(user_text)
        print("Tłumaczenie:", translation, "\n")

if __name__ == '__main__':
    main()
