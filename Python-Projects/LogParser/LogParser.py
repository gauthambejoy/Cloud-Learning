import subprocess
def get_journalctl():
    num_line=int(input("Enter the number of lines:"))
    result=subprocess.run(["journalctl","-n",str(num_line)], capture_output=True, text=True)
    return result.stdout.splitlines()

# get_journalctl()

def parse_log(log_lines):
    counts={
        "ERROR":0,
        "WARNING":0,
        "INFO":0
    }
    for line in log_lines:
        line=line.lower()
        if "error" in line:
            counts["ERROR"]+=1
        elif "warning" in line:
            counts["WARNING"]+=1
        elif "info" in line:
            counts["INFO"]+=1
    return counts

# parse_log()
        
