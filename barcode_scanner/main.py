import evdev
import time
def main():
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    print(devices)
1   print(len(devices))
    for device in devices:
        print(device.path, device.name, device.phys)
        time.sleep(1)
    device = evdev.InputDevice('/dev/input/event0')
    for event in device.read_loop():
     if event.type == evdev.ecodes.EV_KEY:
        print(evdev.categorize(event))


if __name__ == '__main__':
    main()
    