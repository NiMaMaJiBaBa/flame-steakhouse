"""
焰牛排館 (FLAME STEAKHOUSE) - 本地伺服器一鍵啟動腳本
自動啟動本地 Web Server 並在預設瀏覽器中開啟首頁。
"""
import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def run():
    os.chdir(DIRECTORY)
    port = PORT
    server = None
    
    # Try PORT, fallback to next ports if occupied
    for p in range(PORT, PORT + 20):
        try:
            socketserver.TCPServer.allow_reuse_address = True
            server = socketserver.TCPServer(("", p), Handler)
            port = p
            break
        except OSError:
            continue

    if not server:
        print("無法綁定端口，請關閉其他佔用程式後重試。")
        sys.exit(1)

    url = f"http://localhost:{port}/"
    print("=" * 60)
    print(" 🔥 焰牛排館 FLAME STEAKHOUSE 官方網站已成功啟動！")
    print(f" 🌐 本地網址：{url}")
    print(f" 📂 運行目錄：{DIRECTORY}")
    print(" 💡 提示：按 Ctrl+C 可停止伺服器")
    print("=" * 60)

    # Automatically open browser
    try:
        webbrowser.open(url)
    except Exception as e:
        print(f"無法自動開啟瀏覽器，請手動複製連結開啟：{url}")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n伺服器已安全停止。")
        server.server_close()

if __name__ == "__main__":
    run()

