from pydub import AudioSegment

# Carrega o arquivo de áudio 'beat.wav'
audio_segment = AudioSegment.from_wav('beat.wav')

# Exibe o tipo e as informações do áudio carregado
print(type(audio_segment))
print(audio_segment)

# Reverte o áudio e exporta para 'reversed.wav'
reversed_audio = audio_segment.reverse()
reversed_audio.export('reversed.wav')

# Adiciona 15 milissegundos de silêncio ao áudio revertido
reversed_audio = reversed_audio + 15

# print(dir(original))

# Extrai os primeiros 2000 milissegundos (2 segundos) do áudio original e exporta para 'first_two.wav'
first_two_seconds = audio_segment[0:2000]
first_two_seconds.export('first_two.wav')

# Exibe a duração total do áudio original em milissegundos
print(len(audio_segment))

# Cria um áudio combinado que é o áudio original duplicado, seguido por 1000 milissegundos de silêncio e o áudio revertido
merged_audio = audio_segment * 2 + AudioSegment.silent(1000) + reversed_audio
merged_audio.export('merged.wav')
