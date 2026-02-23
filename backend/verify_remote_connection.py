"""
Verify PostgreSQL Remote Access Configuration

This script checks if your PostgreSQL is properly configured for remote access.
Run this AFTER completing the setup steps in docs/POSTGRESQL_REMOTE_SETUP.md
"""

import socket
import subprocess
import sys
import os
from pathlib import Path

def print_header(text):
    """Print a formatted header"""
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60)

def print_status(check_name, passed, message=""):
    """Print check status"""
    status = "✅ PASS" if passed else "❌ FAIL"
    print(f"\n{status} - {check_name}")
    if message:
        print(f"    {message}")

def get_local_ip():
    """Get the local IP address"""
    try:
        # Create a socket to determine local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception as e:
        return None

def check_postgresql_service():
    """Check if PostgreSQL service is running"""
    try:
        result = subprocess.run(
            ['sc', 'query', 'postgresql-x64-14'],
            capture_output=True,
            text=True,
            timeout=5
        )
        return 'RUNNING' in result.stdout
    except Exception:
        # Try alternative service name
        try:
            result = subprocess.run(
                ['sc', 'query', 'postgresql-x64-15'],
                capture_output=True,
                text=True,
                timeout=5
            )
            return 'RUNNING' in result.stdout
        except Exception:
            return False

def check_port_listening():
    """Check if PostgreSQL is listening on port 5432"""
    try:
        result = subprocess.run(
            ['netstat', '-an'],
            capture_output=True,
            text=True,
            timeout=5
        )
        return ':5432' in result.stdout and 'LISTENING' in result.stdout
    except Exception:
        return False

def check_local_connection():
    """Check if local connection works"""
    try:
        # Try to connect using psql
        result = subprocess.run(
            ['psql', '-U', 'postgres', '-d', 'trajectory', '-c', 'SELECT 1;'],
            capture_output=True,
            text=True,
            timeout=10,
            env={**os.environ, 'PGPASSWORD': '8088'}
        )
        return result.returncode == 0
    except Exception:
        return False

def check_firewall_rule():
    """Check if firewall rule exists for port 5432"""
    try:
        result = subprocess.run(
            ['netsh', 'advfirewall', 'firewall', 'show', 'rule', 'name=all'],
            capture_output=True,
            text=True,
            timeout=10
        )
        return '5432' in result.stdout or 'PostgreSQL' in result.stdout
    except Exception:
        return False

def main():
    print_header("PostgreSQL Remote Access Configuration Checker")
    print("\nThis script verifies your PostgreSQL remote access setup.")
    print("Make sure you've completed all steps in docs/POSTGRESQL_REMOTE_SETUP.md")
    
    # Check 1: Get local IP
    print_header("Check 1: Network Configuration")
    local_ip = get_local_ip()
    if local_ip:
        print_status("Local IP Address", True, f"Your IP: {local_ip}")
        print(f"\n    Share this IP with remote users: {local_ip}")
    else:
        print_status("Local IP Address", False, "Could not determine local IP")
    
    # Check 2: PostgreSQL Service
    print_header("Check 2: PostgreSQL Service")
    service_running = check_postgresql_service()
    if service_running:
        print_status("PostgreSQL Service", True, "Service is running")
    else:
        print_status("PostgreSQL Service", False, "Service is not running or not found")
        print("\n    Action: Start PostgreSQL service")
        print("    Run: services.msc → Find postgresql-x64-14 → Start")
    
    # Check 3: Port Listening
    print_header("Check 3: Port Configuration")
    port_listening = check_port_listening()
    if port_listening:
        print_status("Port 5432 Listening", True, "PostgreSQL is listening on port 5432")
    else:
        print_status("Port 5432 Listening", False, "Port 5432 is not listening")
        print("\n    Action: Check postgresql.conf")
        print("    Ensure: listen_addresses = '*'")
        print("    Then restart PostgreSQL service")
    
    # Check 4: Local Connection
    print_header("Check 4: Database Connection")
    local_connection = check_local_connection()
    if local_connection:
        print_status("Local Connection", True, "Can connect to trajectory database")
    else:
        print_status("Local Connection", False, "Cannot connect to database")
        print("\n    Action: Verify database exists and credentials are correct")
        print("    Database: trajectory")
        print("    Username: postgres")
        print("    Password: 8088")
    
    # Check 5: Firewall Rule
    print_header("Check 5: Windows Firewall")
    firewall_rule = check_firewall_rule()
    if firewall_rule:
        print_status("Firewall Rule", True, "Firewall rule found for PostgreSQL")
    else:
        print_status("Firewall Rule", False, "No firewall rule found")
        print("\n    Action: Create firewall rule")
        print("    Run: wf.msc → New Inbound Rule → Port 5432")
    
    # Summary
    print_header("Summary")
    
    all_checks = [
        ("Local IP", local_ip is not None),
        ("PostgreSQL Service", service_running),
        ("Port Listening", port_listening),
        ("Local Connection", local_connection),
        ("Firewall Rule", firewall_rule)
    ]
    
    passed = sum(1 for _, status in all_checks if status)
    total = len(all_checks)
    
    print(f"\nPassed: {passed}/{total} checks")
    
    if passed == total:
        print("\n✅ All checks passed! Your PostgreSQL is ready for remote access.")
        print(f"\nConnection details to share:")
        print(f"  Host: {local_ip}")
        print(f"  Port: 5432")
        print(f"  Database: trajectory")
        print(f"  Username: postgres")
        print(f"  Password: 8088")
        print(f"\nConnection string:")
        print(f"  postgresql://postgres:8088@{local_ip}:5432/trajectory")
    else:
        print("\n⚠️ Some checks failed. Please review the failed checks above.")
        print("Refer to docs/POSTGRESQL_REMOTE_SETUP.md for detailed instructions.")
    
    print("\n" + "=" * 60 + "\n")

if __name__ == "__main__":
    main()
