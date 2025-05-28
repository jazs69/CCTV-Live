import cv2

class VideoCamera:
    def __init__(self):
        # Use 0 for default camera; replace with IP camera URL if needed
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        if not success:
            return None
        # Encode frame as JPEG
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
