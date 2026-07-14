import sounddevice as sd
import soundfile as sf
from kokoro_onnx import Kokoro

# 1. Initialize the offline Kokoro engine
# Ensure the model and voice bin files are in your "lib" directory
kokoro = Kokoro("lib/kokoro-v1.0.int8.onnx", "lib/voices-v1.0.bin")

# 2. Set up your TikTok-like text and speed
text = "Wait, don't scroll! Did you know that cats actually spend 70% of their lives sleeping?"
speed = 1.25  # Slightly sped up for that signature TikTok pacing

# 3. Generate the audio
# "af_heart" is a popular, highly-expressive female voice.
# Other popular presets: 'af_sarah', 'am_adam' (male), 'am_michael' (male)
samples, sample_rate = kokoro.create(
    text, 
    voice="am_adam", 
    speed=speed, 
    lang="en-us"
)

# 4. Save the generated audio as a WAV file
output_filename = "tiktok_voice_offline.wav"
sf.write(output_filename, samples, sample_rate)
print(f"✨ Audio saved successfully as {output_filename}")

# 5. Play it right now through your speakers
print("🔊 Playing audio...")
sd.play(samples, sample_rate)
sd.wait()  # Wait until the audio finishes playing