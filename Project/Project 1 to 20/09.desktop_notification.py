from plyer import notification
import time

if __name__ == "__main__":
    while True:
        notification.notify(
            title="*** Take a Break ***",
            message="Time to take a short rest!",
            app_icon="icon.jpg",  # Ensure this path is correct
            timeout=5,
        )
        time.sleep(10)  # Wait for 10 seconds before the next notification
