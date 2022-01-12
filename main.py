import time

from plyer import notification

if __name__ == '__main__':
    time.sleep(30 * 60)
    run = 0

    while run < 3:
        notification.notify(
            title="Drink Water",
            message="Drink at least a glass of water\nRemember your body needs fuel",
            timeout=30
        )

        time.sleep(60 * 60)
        run += 1

