import paramiko, os

SERVER_IP = "47.92.39.184"
USERNAME = "root"
PASSWORD="2008716fzyFZY."
LOCAL_DIST = r"D:\blog\dist"
REMOTE_WEB = "/var/www/blog"
CERT_DIR = r"D:\blog\lincun.linjie.online_1783593125"
REMOTE_CERT = "/etc/nginx/ssl"

NGINX_CONF = """server {
    listen 80;
    listen [::]:80;
    server_name lincun.linjie.online;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name lincun.linjie.online;

    ssl_certificate /etc/nginx/ssl/lincun.linjie.online.pem;
    ssl_certificate_key /etc/nginx/ssl/lincun.linjie.online.key;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;

    root /var/www/blog;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }

    location /_astro/ {
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    gzip on;
    gzip_types text/plain text/css application/json application/javascript text/xml;
    gzip_min_length 256;
}
"""

def ssh_connect():
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(SERVER_IP, port=22, username=USERNAME, password=PASSWORD, timeout=15)
    return c

def run(c, cmd):
    _, stdout, stderr = c.exec_command(cmd, timeout=120)
    out = stdout.read().decode().strip()
    err = stderr.read().decode().strip()
    if out: print(f"    {out[:300]}")
    if err and "Warning" not in err and "not found" not in err: print(f"    ! {err[:300]}")

def upload_dir(sftp, local_dir, remote_dir):
    try: sftp.mkdir(remote_dir)
    except: pass
    for item in os.listdir(local_dir):
        lp = os.path.join(local_dir, item)
        rp = remote_dir + "/" + item
        if os.path.isdir(lp):
            upload_dir(sftp, lp, rp)
        else:
            sftp.put(lp, rp)
            print(f"    {item}")

client = ssh_connect()

print("Certs...")
sftp = client.open_sftp()
try: sftp.mkdir(REMOTE_CERT)
except: pass
for f in os.listdir(CERT_DIR):
    sftp.put(os.path.join(CERT_DIR, f), f"{REMOTE_CERT}/{f}")
    print(f"    {f}")
sftp.close()

print("Files...")
run(client, f"rm -rf {REMOTE_WEB} && mkdir -p {REMOTE_WEB}")
sftp = client.open_sftp()
upload_dir(sftp, LOCAL_DIST, REMOTE_WEB)
sftp.close()

print("Nginx...")
sftp = client.open_sftp()
with sftp.open("/etc/nginx/sites-available/default", "w") as f:
    f.write(NGINX_CONF)
sftp.close()

run(client, "nginx -t")
run(client, "systemctl reload nginx")

_, stdout, _ = client.exec_command("curl -sk -o /dev/null -w '%{http_code}' https://localhost -H 'Host: lincun.linjie.online'", timeout=10)
print(f"Status: {stdout.read().decode().strip()}")

client.close()
print("Done! https://lincun.linjie.online")
