from datetime import datetime
def main(session): #snowflake passes a session object here
    today = datetime.now()
    date_str = today.strftime("%d%b%y")
    return f"today is {date_str}"