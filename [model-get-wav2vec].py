from transformers import Wav2Vec2ForPreTraining, Wav2Vec2Processor

model_name = 'facebook/wav2vec2-base-960h'

model = Wav2Vec2ForPreTraining.from_pretrained(model_name)
processor = Wav2Vec2Processor.from_pretrained(model_name)

_ = model.save_pretrained("./model-dir")
_ = processor.save_pretrained("./model-dir")