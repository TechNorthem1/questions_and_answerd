import winsound
import time

def tu_funcion():
    # ... tu código ...
    time.sleep(5)  # Simulando una tarea que tarda 5 segundos

if __name__ == "__main__":

    frequency = 2500  # Set Frequency in Hertz, e.g., 2500 Hertz
    duration = 1000  # Set Duration in milliseconds, e.g., 1000 ms == 1 second
    winsound.Beep(frequency, duration)