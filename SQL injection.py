
 import validate_input
 import parse_sql
 import connect_db
 import send_alert

def detect_sql_injection(user_input):
    if validate_input(user_input):
        parsed_sql = parse_sql(user_input)
        if parsed_sql['is_injection'):
            send_alert(parsed_sql)
            return "SQL Injection Detected"
        else:
            connect_db(parsed_sql)
            return "Safe SQL Query"
    else:
        return "Invalid Input"
