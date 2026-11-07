import platform
import subprocess
import shutil
import datetime

def get_system_info():
    print("Gathering System Information...")
    os_name = f"Operating System: {platform.system()} {platform.release()}"
    architecture = f"Architecture: {platform.machine()}"
    
    # Check C: Drive space (Windows)
    total, used, free = shutil.disk_usage("C:\\")
    free_gb = free // (2**30)
    total_gb = total // (2**30)
    disk_space = f"C: Drive Space: {free_gb} GB free of {total_gb} GB total"
    
    return f"{os_name}\n{architecture}\n{disk_space}\n"

def run_network_diagnostics():
    print("Running Network Diagnostics (Pinging 8.8.8.8)...")
    try:
        # Runs a 4-packet ping to Google's public DNS
        ping_output = subprocess.check_output(['ping', '-n', '4', '8.8.8.8'], stderr=subprocess.STDOUT, text=True)
        return f"Network Ping Results:\n{ping_output}"
    except subprocess.CalledProcessError as e:
        return f"Network Ping Failed:\n{e.output}"

def flush_dns():
    print("Flushing DNS Cache...")
    try:
        # Using the exact Windows path ensures Python always finds the tool
        output = subprocess.check_output(
            r'C:\Windows\System32\ipconfig.exe /flushdns', 
            stderr=subprocess.STDOUT, 
            text=True, 
            shell=True
        )
        return "DNS Cache flushed successfully.\n"
    except subprocess.CalledProcessError as e:
        return f"Failed to flush DNS cache. Windows Error:\n{e.output}\n"
    except Exception as e:
        return f"System Python Error:\n{str(e)}\n"

def generate_log():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"L1_Diagnostic_Log_{timestamp}.txt"
    
    print(f"Generating log file: {filename}...")
    
    with open(filename, "w") as file:
        file.write("=== L1 SYSTEM DIAGNOSTIC LOG ===\n")
        file.write(f"Generated on: {timestamp}\n\n")
        
        file.write("--- SYSTEM INFO ---\n")
        file.write(get_system_info() + "\n")
        
        file.write("--- NETWORK DIAGNOSTICS ---\n")
        file.write(run_network_diagnostics() + "\n")
        
        file.write("--- AUTOMATED FIXES ---\n")
        file.write(flush_dns() + "\n")
        
    print(f"Diagnostics complete. Please review {filename}.")

if __name__ == "__main__":
    generate_log()