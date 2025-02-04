import datetime
import time

# User input for blocking duration
block_duration = int(input("Enter blocking duration in minutes: "))
end_time = datetime.datetime.now() + datetime.timedelta(minutes=block_duration)

# User input for sites to block
site_block = []
while True:
    site = input("Enter website to block (or type 'done' to finish): ")
    if site.lower() == "done":
        break
    site_block.append(site)

host_path = "/etc/hosts"  # Use this for system-wide blocking
redirect_url = "192.168.1.72"

while True:
    if datetime.datetime.now() < end_time:
        print("Start blocking")
        with open(host_path, "r+") as host_file:
            content = host_file.read()
            for website in site_block:
                if website not in content:
                    host_file.write(f"{redirect_url} {website}\n")
        time.sleep(5)
    else:
        print("Unblocking sites")
        with open(host_path, "r") as host_file:
            lines = host_file.readlines()
        with open(host_path, "w") as host_file:
            for line in lines:
                if not any(website in line for website in site_block):
                    host_file.write(line)
        break

    time.sleep(5)
