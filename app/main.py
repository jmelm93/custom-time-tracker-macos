from tracker import ApplicationTracker
from logger import init_db

def main():
    init_db()
    tracker = ApplicationTracker()
    tracker.start_tracking()

if __name__ == "__main__":
    main()