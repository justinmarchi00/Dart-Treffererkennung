from cameras.camera import Camera


class CameraManager:

    MAX_CAMERAS = 5

    def __init__(self):
        self.cameras = {}

    def scan_cameras(self):

        self.cameras.clear()

        for i in range(self.MAX_CAMERAS):

            camera = Camera(i)

            if camera.start():

                self.cameras[i] = camera

    def get_camera_information(self):

        result = []

        for cam_id, cam in self.cameras.items():

            result.append({
                "id": cam_id,
                "connected": True,
                "width": cam.width,
                "height": cam.height,
                "fps": cam.fps
            })

        return result

    def get_camera(self, camera_id):
        return self.cameras.get(camera_id)