import subprocess

def audio_out(audio_str):
    """Generate audio out with eSpeak
    """
    # need to pass eSpeak options
    # bluetooth option
    p = subprocess.Popen(["C:\\eSpeak.exe",audio_str])
    return




 



