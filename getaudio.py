import pyaudio

pyaudio_instance = pyaudio.PyAudio()

print('\navailable devices:')

for i in range(pyaudio_instance.get_device_count()):
    dev = pyaudio_instance.get_device_info_by_index(i)
    if (dev['hostApi'] == 0 and dev['maxOutputChannels'] == 0):
        print(i, dev['name'], dev['maxInputChannels'])

print('\ndefault input & output device:')
print(pyaudio_instance.get_default_input_device_info())
print(pyaudio_instance.get_default_output_device_info())
