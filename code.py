import re
import matplotlib.pyplot as plt

ecount = [ 0,0,0,0,0,0,0,0,0,0]

def parse_log_line(log_line):
    m = re.split("\s",log_line,3)
    j=int(m[2])

    if j>=0 and j<10:
        ecount[j]+=1
        return {
            'date': m[0],
            'time': m[1],
            'log_level': m[2],
            'message': m[3]
        }
    else:
        return None

def analyze_logs(log_file_path):
    try:
        with open(log_file_path, 'r') as log_file:
            for log_line in log_file:
                log_entry = parse_log_line(log_line)
                if log_entry:
                    # Perform analysis on the log entry
                    # Example: Print the parsed log entry
                    print(log_entry)
    except FileNotFoundError:
        print(f"File not found: {log_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def plot_bargraph(ecount):
    d={}
    k=[x for x in range(10)]
    myDict = dict(zip(k, ecount))
    fig = plt.figure(figsize = (10, 5))
    plt.bar(k, ecount, color ='maroon', width = 0.4)
    plt.xlabel("Error Level")
    plt.ylabel("No. of Errors")
    plt.title("Error Level Vs Error Count")
    plt.show()


# Example usage
log_file_path = "C:/Users/kavin/OneDrive/Desktop/OS(files)/Log1.txt"
for i in range(10):
    ecount[i]=0
analyze_logs(log_file_path)
plot_bargraph(ecount)
