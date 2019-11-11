PLACEHOLDER = ["Activity", "Video", "Audio", 10]
THEME = "тематика"

def default(name, count=1, last=True, attn=5, available=None, audio_only=True):
    return [name, count, last, attn, available, audio_only]
