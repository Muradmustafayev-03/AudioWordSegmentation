import time

import IPython.display as ipd


def play_audio(array, sr=None):
    """Play Audio with IPython.display.Audio

    :param array: Audio array
    :type array: numpy.ndarray
    :param sr: Sampling rate
    :type sr: int
    """
    ipd.display(ipd.Audio(array, rate=sr, autoplay=True))


def listen_to_segments(words, sr=None):
    """Listen to audio segments

    :param words: List of audio segments
    :type words: list of numpy.ndarray
    :param sr: Sampling rate
    :type sr: int
    """
    for i, word in enumerate(words):
        print(f'Listening to Word {i + 1}')
        play_audio(word, sr=sr)
        time.sleep(1)
