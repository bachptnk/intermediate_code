from transformers import Tokenizer, Model

model_name = 'gpt2-xl'

model = Tokenizer.from_pretrained(model_name)
processor = Model.from_pretrained(model_name)

_ = model.save_pretrained("./model-dir")
_ = processor.save_pretrained("./model-dir")