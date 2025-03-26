import time
from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput
import os

user= os.getlogin()

user_home = os.path.expanduser(f'~{user}')

camera = Picamera2()

preview_config = camera.preview_configuration

try:
    preview_config.size= (800,600)
    preview_config.format = 'XRGB8888'
    camera.start_preview(Preview.QTGL)
    
    conf = {'size': (800,600)}
    controls = {'FrameRate': 40}
    config = camera.create_video_configuration(main= conf, controls = controls, buffer_count = 12)
    
    encoder = H264Encoder(bitrate=10000000)
    output = FfmpegOutput(f'{user_home}/my_video.mp4')
    
    camera.configure(config)
    camera.start_recording(encoder,output)
    
    time.sleep(10)
    camera.stop_recording()
    
except KeyboardInterrupt:
    camera.stop_preview()
    pass