import librosa.display
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use('TkAgg')


def plot_audio(y, sr):
    plt.figure(figsize=(12, 8))
    librosa.display.waveshow(y, sr=sr)
    plt.title('Audio Waveform')
    plt.show()


def plot_segmentation(audio_path, segments, words):
    y, sr = librosa.load(audio_path)

    plt.figure(figsize=(14, 5))
    plt.plot(y, label='Original Audio')
    plt.vlines(np.where(segments)[0], ymin=min(y), ymax=max(y), color='r', linestyle='--', label='Speech Segments')
    plt.title('Audio Segmentation')
    plt.legend()
    plt.show()

    # Plot individual words
    for i, word in enumerate(words):
        plt.figure(figsize=(14, 2))
        plt.plot(word)
        plt.title(f'Word {i + 1}')
        plt.show()


def plot_waveform_and_energy(y, sr, energy, threshold):
    plt.figure(figsize=(12, 8))

    plt.subplot(2, 1, 1)
    librosa.display.waveshow(y, sr=sr)
    plt.title('Audio Waveform')

    plt.subplot(2, 1, 2)
    librosa.display.specshow(energy, x_axis='time', sr=sr)
    plt.axhline(y=threshold, color='r', linestyle='--', label='Energy Threshold')
    plt.title('Short-term Energy')
    plt.colorbar(format='%+2.0f dB')
    plt.tight_layout()

    plt.show()
