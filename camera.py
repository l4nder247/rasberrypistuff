from picamera2 import PiCamera2, Preview
import os
user = os.getlogin()
user_home = os.path.expanderuser(f'~{user}')

camera = PiCamera2()
preview_config = camera.preview_configuration

try:
    preview_config.size= (800,800)

    preview_config.format = 'XRGB8888'

    camera.start_preview(Preview.QTGL)

    camera.start()

    camera.capture_file(f'{user_home}/my_photo.jpg')

except KeyboardInterrupt:
    camera.stop_preview()
    pass