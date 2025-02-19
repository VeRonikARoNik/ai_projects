
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
import os
from transformers import T5ForConditionalGeneration, T5Tokenizer

# Jeśli korzystasz z GPU, ustaw device = 'cuda', w przeciwnym razie 'cpu'
device = 'cpu'
# Jeśli masz problemy z OpenMP, możesz odkomentować poniższą linię:
# os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

model_name = 'utrobinmv/t5_translate_en_ru_zh_small_1024'
model = T5ForConditionalGeneration.from_pretrained(model_name)
model.to(device)
tokenizer = T5Tokenizer.from_pretrained(model_name)

print("Tłumacz AI: Wpisuj tekst po angielsku, a otrzymasz tłumaczenia na chiński i rosyjski.")
print("Wpisz 'exit', aby zakończyć.")

while True:
    user_input = input("\nWprowadź tekst: ").strip()
    if user_input.lower() == 'exit':
        break

    # Tłumaczenie na chiński
    prefix_zh = 'translate to zh: '
    src_text_zh = prefix_zh + user_input
    input_ids_zh = tokenizer(src_text_zh, return_tensors="pt").to(device)
    generated_tokens_zh = model.generate(**input_ids_zh)
    result_zh = tokenizer.batch_decode(generated_tokens_zh, skip_special_tokens=True)[0]

    # Tłumaczenie na rosyjski
    prefix_ru = 'translate to ru: '
    src_text_ru = prefix_ru + user_input
    input_ids_ru = tokenizer(src_text_ru, return_tensors="pt").to(device)
    generated_tokens_ru = model.generate(**input_ids_ru)
    result_ru = tokenizer.batch_decode(generated_tokens_ru, skip_special_tokens=True)[0]

    print(f"\n[Tłumaczenie na chiński]:\n{result_zh}")
    print(f"\n[Tłumaczenie na rosyjski]:\n{result_ru}")

print("Koniec programu.")
