from transformers import AutoModelForCausalLM, AutoTokenizer



tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-large")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-large")

_ = tokenizer.save_pretrained("./model-dir")
_ = model.save_pretrained("./model-dir")


