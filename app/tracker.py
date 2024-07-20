import time
from Quartz import CGWindowListCopyWindowInfo, kCGWindowListOptionOnScreenOnly, kCGNullWindowID
from logger import log_to_db
from context_builder import context_builder

class ApplicationTracker:
    def __init__(self, interval=5, db_path='activity_log.db'):
        self.interval = interval
        self.start_time = time.time()
        self.last_app = None
        self.last_context = None
        self.db_path = db_path

    def get_active_window(self):
        window_list = CGWindowListCopyWindowInfo(kCGWindowListOptionOnScreenOnly, kCGNullWindowID)
        for window in window_list:
            if window['kCGWindowLayer'] == 0:
                app = window['kCGWindowOwnerName']
                title = window.get('kCGWindowName', 'Unknown')
                print(f"Active window: app={app}, title={title}")
                return app, title
        return None, None

    def get_context(self, app):
        return context_builder(app)

    def start_tracking(self):
        while True:
            time.sleep(self.interval)
            current_app, current_context = self.get_active_window()
            if current_app != self.last_app or current_context != self.last_context:
                end_time = time.time()
                log_to_db(self.start_time, end_time, self.last_app, self.last_context, db_path=self.db_path)
                self.start_time = end_time
                self.last_app, self.last_context = current_app, self.get_context(current_app)
                print(f"Switching to app: {current_app} with context: {current_context}")