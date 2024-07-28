from pydub import AudioSegment

# Carrega os arquivos de áudio 'beat.wav' e 'sax.wav'
beat_audio = AudioSegment.from_wav('beat.wav')
sax_audio = AudioSegment.from_wav('sax.wav')

# Exibe a duração dos áudios 'beat.wav' e 'sax.wav' em milissegundos
print(len(beat_audio), len(sax_audio))

# Duplica o áudio de batida e exporta para 'beat2.wav'
beat_audio_doubled = beat_audio * 2
beat_audio_doubled.export('beat2.wav')

# Sobrepõe o áudio de sax na batida duplicada e exporta para 'mixed.wav'
mixed_audio = beat_audio_doubled.overlay(sax_audio)
mixed_audio.export('mixed.wav')

# Cria um áudio final combinando a batida duplicada, o áudio misturado repetido duas vezes, o áudio de sax, a batida duplicada novamente e o áudio de sax
final_audio = beat_audio_doubled + mixed_audio * 2 + sax_audio + beat_audio_doubled + sax_audio
final_audio.export('final.wav')