# PostgreSQL Connection Information

**Database:** Trajectory Student Management System

---

## Connection Details

```
Host: [YOUR_IP_ADDRESS]
Port: 5432
Database: trajectory
Username: postgres
Password: 8088
```

---

## Connection String

```
postgresql://postgres:8088@[YOUR_IP_ADDRESS]:5432/trajectory
```

---

## For Python Applications

```python
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:8088@[YOUR_IP_ADDRESS]:5432/trajectory"
engine = create_engine(DATABASE_URL)
```

---

## For psql Command Line

```bash
psql -h [YOUR_IP_ADDRESS] -U postgres -d trajectory
```

When prompted, enter password: `8088`

---

## For pgAdmin

1. Right-click "Servers" → Create → Server
2. General tab:
   - Name: `Trajectory Remote`
3. Connection tab:
   - Host: `[YOUR_IP_ADDRESS]`
   - Port: `5432`
   - Database: `trajectory`
   - Username: `postgres`
   - Password: `8088`
4. Click "Save"

---

## Testing Connection

### Quick Test
```bash
psql -h [YOUR_IP_ADDRESS] -U postgres -d trajectory -c "SELECT version();"
```

### Python Test
```python
import psycopg2

try:
    conn = psycopg2.connect(
        host="[YOUR_IP_ADDRESS]",
        port=5432,
        database="trajectory",
        user="postgres",
        password="8088"
    )
    print("✅ Connection successful!")
    conn.close()
except Exception as e:
    print(f"❌ Connection failed: {e}")
```

---

## Network Requirements

- Both computers must be on the same local network (WiFi/LAN)
- Firewall must allow port 5432
- PostgreSQL must be configured for remote access

---

## Security Notes

- This setup is for development/testing on a local network
- Do not expose this database to the public internet
- Change the password for production use
- Consider using SSL/TLS for production environments

---

## Troubleshooting

### Cannot Connect
1. Verify both PCs are on same network
2. Check firewall allows port 5432
3. Confirm PostgreSQL service is running
4. Verify IP address is correct (use `ipconfig`)

### Authentication Failed
1. Verify password is `8088`
2. Check pg_hba.conf allows your IP
3. Restart PostgreSQL service after config changes

### Connection Timeout
1. Check Windows Firewall settings
2. Verify router is not blocking traffic
3. Try pinging the host: `ping [YOUR_IP_ADDRESS]`

---

**Last Updated:** [DATE]
**Setup Guide:** See `docs/POSTGRESQL_REMOTE_SETUP.md`
