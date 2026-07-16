# 🗣️ Kokoro Offline TTS

> A simple, fast, and completely offline Text-to-Speech (TTS) web app — built with Python 3, Flask, and Kokoro ONNX.

No internet connection, no API keys, no GPU required. Just type your text, pick a voice, and generate natural-sounding speech locally on your machine.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Backend-black?logo=flask&logoColor=white)
![License](https://img.shields.io/badge/Offline-100%25-success)
![No GPU](https://img.shields.io/badge/GPU-Not%20Required-informational)

---

## ✨ Features

- 🎙️ **Offline speech synthesis** — no cloud services, no internet needed after setup
- 🌍 **Multi-language support** — 7 languages and accents out of the box
- 🎚️ **Adjustable playback speed** — from `0.5x` to `2.0x`, in `0.05` increments
- ⬇️ **One-click download** — save generated audio as a `.wav` file
- 💻 **Lightweight** — runs comfortably with as little as 500MB free RAM
- 🚫 **No GPU required** — runs entirely on CPU
- 🎨 **Modern, clean UI** — dark-themed, responsive web interface

---

## 🌍 Supported Languages

| Language | Accent |
|---|---|
| 🇺🇸 English | American |
| 🇬🇧 English | British |
| 🇵🇹 Portuguese | — |
| 🇫🇷 French | — |
| 🇮🇳 Hindi | — |
| 🇮🇹 Italian | — |
| 🇪🇸 Spanish | — |

---

## ⚙️ Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3 |
| Web Framework | [Flask](https://flask.palletsprojects.com/) |
| Audio Processing | [soundfile](https://pysoundfile.readthedocs.io/) |
| TTS Engine | [kokoro_onnx](https://github.com/thewh1teagle/kokoro-onnx) |

---

## 📋 Requirements

- **Python** 3.x
- **RAM:** Minimum 500MB free
- **GPU:** Not required — runs entirely on CPU
- **Disk space:** Varies — generated audio accumulates in the `Generated_Audios` folder (see [Notes](#-notes))

---

## 🧩 Model Files Setup

This project relies on the **Kokoro** TTS model files, which are **not included** in the repository due to their size. You need to download them manually before running the app.

**Download the following files:**

| File | Size | Link |
|---|---|---|
| `kokoro-v1.0.int8.onnx` | ~88MB | [Download](https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.int8.onnx) |
| `voices-v1.0.bin` | ~27MB | [Download](https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin) |

> ℹ️ These are the quantized (int8) model files, chosen for lower RAM usage and CPU-only inference. Full precision (`kokoro-v1.0.onnx`, 310MB) and half precision (`kokoro-v1.0.fp16.onnx`, 169MB) variants are also available on the [kokoro-onnx releases page](https://github.com/thewh1teagle/kokoro-onnx/releases/tag/model-files-v1.0) if you prefer higher fidelity.

**Place both files inside:**

```
kokoro-web/
└── lib/
    ├── kokoro-v1.0.int8.onnx
    └── voices-v1.0.bin
```

Or via terminal:

```bash
mkdir -p kokoro-web/lib
mv kokoro-v1.0.int8.onnx voices-v1.0.bin kokoro-web/lib/
```
---

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/MJTech46/PY-Offline-TTS.git
cd PY-Offline-TTS

# Install dependencies
pip install flask soundfile kokoro_onnx

# Move to the directory
cd kokoro-web

# Run the app
python app.py
```

Then open your browser and navigate to:

```
http://127.0.0.1:5000/
```
---

## 📘 How to Use

1. **Enter your text** in the input box
2. **Select a language** from the dropdown
3. **Select a voice** for that language
4. **Adjust the speed** using the slider (`0.5x`–`2.0x`, step `0.05`)
5. Click **Generate Speech**
6. **Preview** the audio using the built-in player
7. Click the **⬇️ download icon** to save the `.wav` file locally

---

## 📝 Notes

> ⚠️ **Storage:** All generated audio files are saved in the `Generated_Audios` folder. Over time, this folder can grow large — feel free to delete its contents periodically to free up disk space.

---

## 👤 Author

**MJ Tech**

- 🐙 GitHub: [@MJTech46](https://github.com/MJTech46)
- 📦 Repository: [PY-Offline-TTS](https://github.com/MJTech46/PY-Offline-TTS)
- ✉️ Email: [mjtecg46@gmail.com](mailto:mjtecg46@gmail.com)

---

## 🤝 Contributing & Support

Found a bug or have an idea for a new feature? Contributions and suggestions are welcome!

- Open an [issue](https://github.com/MJTech46/PY-Offline-TTS/issues) on GitHub
- Or reach out directly via email: **mjtecg46@gmail.com**

---
## 🙏 Credits & Acknowledgements

This project wouldn't be possible without the following open-source work:

- **[thewh1teagle/kokoro-onnx](https://github.com/thewh1teagle/kokoro-onnx)** — TTS inference using the Kokoro model with the ONNX runtime. The core engine powering the offline speech synthesis in this project.
- **[Kokoro](https://huggingface.co/hexgrad/Kokoro-82M)** — the underlying open-weight TTS model.
- **[Flask](https://flask.palletsprojects.com/)** — the web framework used to serve the app.
- **[soundfile](https://pysoundfile.readthedocs.io/)** — used for reading and writing audio files.

A huge thanks to these authors and maintainers for making their work available to the community. 💙

---

<p align="center">Made with ❤️ by <strong>MJ Tech</strong></p>
