import subprocess
import pathlib

cwd = pathlib.Path(__file__).parent.absolute()

def context_builder(app):
    print(f"Building context for app: {app}")
    if app == 'Google Chrome':
        return run_applescript('get_chrome_url.applescript')
    elif app == 'Slack':
        return run_applescript('get_slack_context.applescript')
    elif app == 'Code':
        return run_applescript('get_code_working_directory.applescript')
    else:
        return None
    

def run_applescript(script_name):
    script_path = cwd / 'applescripts' / script_name
    result = subprocess.run(['osascript', script_path], capture_output=True, text=True)
    if result.returncode == 0:
        return result.stdout.strip()
    else:
        print(f"Error running {script_name}: {result.stderr}")
        return None

