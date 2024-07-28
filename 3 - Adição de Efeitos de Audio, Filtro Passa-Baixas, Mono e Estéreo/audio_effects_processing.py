from pydub import AudioSegment

# Carrega o arquivo de áudio 'beat.wav'
beat_audio = AudioSegment.from_wav('beat.wav')

# Aplica um filtro passa-baixas com frequência de corte de 2000 Hz e exporta para 'beat_low.wav'
beat_audio_low = beat_audio.low_pass_filter(2000)
beat_audio_low.export('beat_low.wav')

# Panorâmica do áudio filtrado para a esquerda e exporta
beat_audio_left = beat_audio_low.pan(-1)

# Panorâmica do áudio filtrado para a direita e exporta
beat_audio_right = beat_audio_low.pan(1)

# Combina o áudio panorâmico à esquerda, o panorâmico à direita e o áudio filtrado, e exporta para 'beat_final.wav'
beat_audio_final = beat_audio_left + beat_audio_right + beat_audio_low
beat_audio_final.export('beat_final.wav')
