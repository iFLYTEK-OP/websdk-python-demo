import pyaudio
import queue
import threading
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AudioPlayer:
    def __init__(self, sample_rate=16000, sample_size_in_bits=16, channels=1, signed=True, big_endian=False):
        self.sample_rate = sample_rate
        self.sample_size_in_bits = sample_size_in_bits
        self.channels = channels
        self.signed = signed
        self.big_endian = big_endian
        self.audio_queue = queue.Queue()
        self.is_playing = False
        self.player_thread = None
        self.stream = None

    def start(self):
        if self.is_playing:
            return
        self.is_playing = True

        self.player_thread = threading.Thread(target=self._play_audio)
        self.player_thread.name = "Audio-Player-Thread"
        self.player_thread.start()

    def _play_audio(self):
        try:
            p = pyaudio.PyAudio()
            format_ = pyaudio.paInt16 if self.signed else pyaudio.paUInt8

            self.stream = p.open(format=format_,
                                 channels=self.channels,
                                 rate=int(self.sample_rate),
                                 output=True,
                                 frames_per_buffer=1024,
                                 stream_callback=None,
                                 start=False,
                                 input_host_api_specific_stream_info=None,
                                 output_host_api_specific_stream_info=None)

            self.stream.start_stream()

            while self.is_playing or not self.audio_queue.empty():
                try:
                    audio_data = self.audio_queue.get(timeout=0.1)
                    self.safe_write(audio_data)
                except queue.Empty:
                    pass
                time.sleep(0.02)

            self.stream.stop_stream()
            self.stream.close()
            p.terminate()
            logger.info("播放器线程正常结束")

        except Exception as e:
            logger.error(str(e), exc_info=True)

    def play(self, audio_data):
        if not self.is_playing:
            raise RuntimeError("AudioPlayer未启动")
        self.audio_queue.put(audio_data)

    def stop(self):
        self.is_playing = False
        if self.player_thread is not None:
            self.player_thread.join()

    def safe_write(self, audio_data):
        frame_size = self.channels * (self.sample_size_in_bits // 8)
        length = len(audio_data)
        remainder = length % frame_size
        if remainder != 0:
            length -= remainder
        self.stream.write(audio_data[:length])
