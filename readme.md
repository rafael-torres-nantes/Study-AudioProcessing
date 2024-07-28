# 🎶 Estudo de Processamento de Áudio

Bem-vindo ao repositório de Estudo de Processamento de Áudio! Este repositório é dedicado ao aprendizado e aplicação de técnicas de processamento de áudio utilizando Python. Aqui, você encontrará exemplos e recursos para trabalhar com diversas operações de áudio, incluindo reversão, alteração de volume, loop, corte, silenciamento, sobreposição e adição de efeitos.

📌 Navegação
- 📝 Sobre o Projeto
- 📦 Instalação e Configuração
- 📁 Estrutura do Repositório
- 🔧 Configuração e Testes

---

## 📝 Sobre o Projeto

Este repositório explora várias técnicas de processamento de áudio usando as bibliotecas `pydub` e `SpeechRecognition`. Abaixo estão algumas das funcionalidades implementadas:

- **Reversão e Alteração de Volume:** Modificar o áudio para criar efeitos variados.
- **Loop e Corte:** Criar loops e cortar partes específicas de um áudio.
- **Silenciamento:** Adicionar silêncio em pontos específicos do áudio.
- **Sobreposição e Mixagem:** Combinar múltiplas faixas de áudio.
- **Adição de Efeitos:** Aplicar filtros e efeitos, como filtro passa-baixas e panorâmica.

## 📦 Instalação e Configuração

Para instalar as bibliotecas necessárias, execute os seguintes comandos:

```bash
pip install pydub
pip install SpeechRecognition
```

### Dependências

- **pydub:** Biblioteca para manipulação de áudio.
  - [Documentação do Pydub](https://github.com/jiaaro/pydub)
- **SpeechRecognition:** Biblioteca para reconhecimento de fala.
  - [Documentação do SpeechRecognition](https://pypi.org/project/SpeechRecognition/)

## 📁 Estrutura do Repositório

O repositório está organizado da seguinte forma:

- **Quatros Pastas:** Cada pasta contém um Scripts e exemplos de manipulação de áudio:
  - `audio_processing_example.py`: Exemplo de reversão e ajuste de volume do áudio.
  - `audio_mixing_and_overlay.py`: Exemplo de sobreposição e mixagem de áudio.
  - `audio_effects_processing.py`: Exemplo de adição de efeitos como filtro passa-baixas e panorâmica.
  - `speech_recognition.py`: Exemplo de reconhecimento de fala usando `SpeechRecognition`.

## 🔧 Configuração e Testes

Certifique-se de que todas as dependências estão instaladas corretamente. Para testar os scripts, você pode usar arquivos de áudio de exemplo (`beat.wav`, `sax.wav`, `chile.wav`) incluídos no repositório.

### Exemplo de Uso

Para usar um dos scripts, como `reversao_volume.py`, você pode executar o seguinte comando no terminal:

```bash
python processamento_audio/reversao_volume.py
```

Isso aplicará as operações definidas no script ao arquivo de áudio especificado.

---

**Cursos Recomendados:**

- [Automate Everything with Python](https://www.udemy.com/course/automate-everything-with-python/)
