from speech_recognition import Recognizer, AudioFile

# Cria uma instância do reconhecedor de fala
speech_recognizer = Recognizer()

# Abre o arquivo de áudio 'chile.wav' para reconhecimento
with AudioFile('chile.wav') as audio_file:
    # Lê o áudio do arquivo
    audio_data = speech_recognizer.record(audio_file)

# Reconhece o texto a partir dos dados de áudio usando o serviço de reconhecimento do Google
recognized_text = speech_recognizer.recognize_google(audio_data)

# Exibe o texto reconhecido
print(recognized_text)
