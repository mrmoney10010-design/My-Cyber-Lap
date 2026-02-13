import subprocess

target = "10.0.2.15"
print(f"🚀starting security scan on {target}...")

results = subprocess.check_output(f"sudo nmap -sV {target}", shell=True).decode()

with open("scan_report.txt", "w") as file:
    file.write(results)

print("✅ scan complete! Results saved to scan_report.txt")  


