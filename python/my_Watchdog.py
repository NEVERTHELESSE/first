import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyEventHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.src_path.endswith('.py'):
            print(f'Restarting due to change in {event.src_path}')
            # Replace with your restart logic
            # Example: you could restart a server or run tests here

if __name__ == '__main__':
    path = '.'  # Replace with the path to monitor
    event_handler = MyEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
