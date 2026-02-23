# PostgreSQL Remote Access Setup - Step by Step Guide

**Project:** Trajectory Database
**Database:** trajectory
**User:** postgres
**Password:** 8088

---

## STEP 1: Find Your IP Address

Open Command Prompt and run:
```cmd
ipconfig
```

Look for **IPv4 Address** under your active network (WiFi or Ethernet).

**Example output:**
```
Wireless LAN adapter Wi-Fi:
   IPv4 Address. . . . . . . . . . . : 192.168.1.100
```

**✏️ Write your IP here:** `_________________`

**✅ Checkpoint:** You have your IP address written down.

---

## STEP 2: Edit postgresql.conf

### 2.1 Locate the File
The file is likely at:
```
C:\Program Files\PostgreSQL\14\data\postgresql.conf
```

Or find it in pgAdmin:
- Right-click your server → Properties → General → Data directory

### 2.2 Open as Administrator
1. Right-click **Notepad**
2. Select **Run as administrator**
3. File → Open → Navigate to `postgresql.conf`

### 2.3 Make the Change
Find this line (around line 59):
```conf
#listen_addresses = 'localhost'
```

Change it to:
```conf
listen_addresses = '*'
```

**Important:** Remove the `#` at the beginning!

### 2.4 Save the File
- File → Save
- Close Notepad

**✅ Checkpoint:** postgresql.conf is saved with `listen_addresses = '*'`

---

## STEP 3: Edit pg_hba.conf

### 3.1 Locate the File
Same directory as before:
```
C:\Program Files\PostgreSQL\14\data\pg_hba.conf
```

### 3.2 Open as Administrator
1. Right-click **Notepad**
2. Select **Run as administrator**
3. File → Open → Navigate to `pg_hba.conf`

### 3.3 Add Remote Access Rule
Scroll to the **bottom** of the file and add ONE of these options:

**Option A - Allow Specific IP (Most Secure):**
```conf
# Allow remote connection from Arun's PC
host    trajectory    postgres    REMOTE_PC_IP/32    md5
```
Replace `REMOTE_PC_IP` with the actual IP address of the remote PC.

**Example:**
```conf
host    trajectory    postgres    192.168.1.50/32    md5
```

**Option B - Allow Any IP on Your Local Network (Easier for Testing):**
```conf
# Allow any PC on local network
host    trajectory    postgres    192.168.1.0/24    md5
```

**Option C - Allow Any IP (Least Secure, Only for Testing):**
```conf
# Allow any IP (testing only)
host    trajectory    postgres    0.0.0.0/0    md5
```

### 3.4 Save the File
- File → Save
- Close Notepad

**✅ Checkpoint:** pg_hba.conf is saved with the new rule at the bottom.

---

## STEP 4: Configure Windows Firewall

### 4.1 Open Firewall Settings
1. Press `Win + R`
2. Type: `wf.msc`
3. Press Enter

### 4.2 Create Inbound Rule
1. Click **Inbound Rules** (left panel)
2. Click **New Rule...** (right panel)
3. Select **Port** → Click **Next**
4. Select **TCP**
5. Enter port: `5432`
6. Click **Next**
7. Select **Allow the connection**
8. Click **Next**
9. Check all three boxes:
   - ☑ Domain
   - ☑ Private
   - ☑ Public
10. Click **Next**
11. Name: `PostgreSQL Remote Access`
12. Click **Finish**

**✅ Checkpoint:** Firewall rule created for port 5432.

---

## STEP 5: Restart PostgreSQL Service

### Method 1: Using Services (Recommended)
1. Press `Win + R`
2. Type: `services.msc`
3. Press Enter
4. Scroll down to find **postgresql-x64-14** (or your version)
5. Right-click → **Restart**
6. Wait for "Status" to show "Running"

### Method 2: Using Command Prompt
Open Command Prompt **as Administrator** and run:
```cmd
net stop postgresql-x64-14
net start postgresql-x64-14
```

**✅ Checkpoint:** PostgreSQL service restarted successfully.

---

## STEP 6: Test Local Connection (Verify It Still Works)

Open Command Prompt and run:
```cmd
cd backend
psql -U postgres -d trajectory
```

Enter password: `8088`

You should see:
```
trajectory=#
```

Type `\q` to exit.

**✅ Checkpoint:** Local connection still works.

---

## STEP 7: Share Connection Details

Send this information to the remote PC:

```
PostgreSQL Connection Details for Trajectory Database
=====================================================
Host: YOUR_IP_ADDRESS (from Step 1)
Port: 5432
Database: trajectory
Username: postgres
Password: 8088

Connection String:
postgresql://postgres:8088@YOUR_IP_ADDRESS:5432/trajectory
```

**✅ Checkpoint:** Connection details shared with remote user.

---

## STEP 8: Remote PC Tests Connection

The remote PC should test with:

```cmd
psql -h YOUR_IP_ADDRESS -U postgres -d trajectory
```

**Example:**
```cmd
psql -h 192.168.1.100 -U postgres -d trajectory
```

If successful, they'll see:
```
Password for user postgres:
trajectory=#
```

**✅ Checkpoint:** Remote connection successful!

---

## Troubleshooting

### Problem: "Connection refused"
**Solutions:**
1. Check PostgreSQL service is running (Step 5)
2. Verify firewall rule exists (Step 4)
3. Confirm IP address is correct (Step 1)

### Problem: "Connection timed out"
**Solutions:**
1. Both PCs must be on the same network
2. Check Windows Firewall is not blocking
3. Try temporarily disabling firewall to test

### Problem: "Authentication failed"
**Solutions:**
1. Verify password is `8088`
2. Check pg_hba.conf has correct IP (Step 3)
3. Restart PostgreSQL after changes (Step 5)

### Problem: "No route to host"
**Solutions:**
1. Verify both PCs are on same WiFi/network
2. Check router is not blocking traffic
3. Try pinging: `ping YOUR_IP_ADDRESS`

---

## Verification Script

After setup, run this from your project:
```cmd
cd backend
python verify_remote_connection.py
```

This will check if remote access is properly configured.

---

## Security Notes

**Current Setup (Development):**
- ✅ Password authentication
- ✅ Local network only
- ✅ Firewall configured

**For Production (Future):**
- Use SSL/TLS encryption
- Use stronger passwords
- Limit to specific IPs only
- Consider VPN for remote access

---

## Reverting Changes

If you need to disable remote access:

1. **Edit postgresql.conf:**
   ```conf
   listen_addresses = 'localhost'
   ```

2. **Edit pg_hba.conf:**
   Comment out or remove the line you added:
   ```conf
   # host    trajectory    postgres    192.168.1.0/24    md5
   ```

3. **Restart PostgreSQL** (Step 5)

---

## Summary Checklist

- [ ] Step 1: Found my IP address
- [ ] Step 2: Edited postgresql.conf
- [ ] Step 3: Edited pg_hba.conf
- [ ] Step 4: Configured Windows Firewall
- [ ] Step 5: Restarted PostgreSQL
- [ ] Step 6: Tested local connection
- [ ] Step 7: Shared connection details
- [ ] Step 8: Remote PC connected successfully

---

**Status:** Ready to begin setup
**Time Required:** 5-10 minutes
**Difficulty:** Easy (just follow each step)
