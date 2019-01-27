import os
import time
from PIL import Image
import anki_vector
from anki_vector.util import degrees


def main():
    with anki_vector.Robot() as robot:
        robot.behavior.set_head_angle(degrees(45.0))
        robot.behavior.set_lift_height(0.0)

        current_directory = os.path.dirname(os.path.realpath(__file__))
        image_path = os.path.join(current_directory, "..", "face_images", "cozmo_image.jpg")

        # Cargamos la imagen
        image_file = Image.open(image_path)

        # Convertimos la imagen a pixels en la pantalla
        screen_data = anki_vector.screen.convert_image_to_screen_data(image_file)

        # Truco para quitar los ojos
        robot.screen.set_screen_to_color(anki_vector.color.off, duration_sec=0.1)

        # Mostramos la imagen 5 segundos
        robot.screen.set_screen_with_image_data(screen_data, 5.0)

        # Sonido Suscríbete
        robot.say_text("soos cree beh teh!")
        time.sleep(0.7)
        # Golpe con la palanca!
        robot.motors.set_lift_motor(5)
        time.sleep(0.1)
        robot.motors.set_lift_motor(0)


if __name__ == "__main__":
    main()
