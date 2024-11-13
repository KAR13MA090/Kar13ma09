<h1 align="center">📡 Kar13ma09 tool</h1> 
<div align="center">

<img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg"> 
</div>

<div align="center">
  <h1>Installation</h1>
  <img src="img/windows.png" width="80" height="80">
  <h2>Windows</h2><br>
</div>
Tải Về Python 3.10 [here](https://www.python.org/downloads/), 
  make setup
  make run
  ```
Nếu bạn không có nó, thì thực hiện:
  ```
  curl -sSL https://install.python-poetry.org | python3
  poetry install --without dev
  poetry run python3 kar13ma09.py
  ```
  ---
<div align="center">
  <br>
  <img src="img/linux.png" width="100" height="80"><h2>Linux</h2><br>
</div>
```
sudo apt update
sudo apt install python3 python3-pip git -y
git clone https://github.com/KAR13MA090/Kar13ma09
cd Kar13ma09/

make setup
make run
```

---
<div align="center">
  <br>
  <img src="img/termux.png" width="50" height="50">
  <h2>Termux</h2><br>
</div>

```
pkg update
pkg install python3 python3-pip git -y

git clone https://github.com/KAR13MA090/Kar13ma09
cd Kar13ma09/

pip install -r requirements.txt
python3 overload.py
```

---
<br>

<div align="center">
  <h2>Các cuộc tấn công có sẵn</h2><br>
</div>

`HTTP`: Cuộc tấn công này bao gồm việc làm kiệt sức nạn nhân bằng cách gửi một lượng lớn yêu cầu HTTP GET, cuối cùng làm cho nó sập và ngăn chặn người khác truy cập vào tài nguyên của nó.

```
├─── DOS TOOL
├─── AVAILABLE METHODS
├─── LAYER 7: HTTP | HTTP-PROXY | SLOWLORIS | SLOWLORIS-PROXY
├───┐
│   ├───METHOD: HTTP
│   ├───TIME: 600
│   ├───THREADS: 800
│   └───URL: https://github.com/KAR13MA090/Kar13ma09
```

`Slowloris`: Just like an HTTP attack, Slowloris also aims to block other users from accessing a certain resource, but it does that by connecting virtual hosts with a slow connection to the victim. The victim will eventually have a lot of slow connections open and will block new users from accessing its resources.

```
...
├───┐
│   ├───METHOD: SLOWLORIS
│   ├───TIME: 300
│   ├───THREADS: 200
│   ├───SLEEP TIME: 15
│   └───URL: https://github.com/7zx/overload
```

Cả tấn công `HTTP` và `Slowloris` đều có phiên bản proxy. Nếu bạn chọn sử dụng proxy, các luồng sẽ khởi tạo và kết nối đến các proxy công khai có độ ẩn danh cao, nếu không, địa chỉ IP của bạn sẽ được sử dụng trong các yêu cầu. Chúng tôi không sở hữu các máy chủ proxy và không chịu trách nhiệm về bất kỳ điều gì mà chúng có thể làm (như rò rỉ địa chỉ IP thực của bạn); chúng được lưu trữ bởi các tình nguyện viên và địa chỉ của chúng được lấy thông qua [Proxy Scrape API](https://docs.proxyscrape.com/).

<br>

## Chỉ tấn công POSIX

Để thực hiện các cuộc tấn công sau, bạn sẽ cần một máy chạy hệ thống POSIX, như Ubuntu.
<br><br>

`SYN-Flood`: Cuộc tấn công này dựa vào cách mà giao thức Điều khiển Truyền tải (TCP) được thiết kế. Nó lợi dụng quy trình bắt tay 3 bước của TCP (SYN, SYN-ACK và ACK) bằng cách gửi rất nhiều gói tin có cờ SYN, nhưng không bao giờ phản hồi lại các gói SYN-ACK được gửi bởi nạn nhân, khiến cho nạn nhân phải chờ đợi mãi mãi với một kết nối mở. Nếu nạn nhân không đóng kết nối được mở bởi các gói SYN, thì cuối cùng nó sẽ chặn các kết nối mới.

```
...
├─── LAYER 4: SYN-FLOOD
├───┐
│   ├───METHOD: SYN-FLOOD
│   ├───TIME: 40
│   ├───THREADS: 10
│   └───URL: 192.168.0.1
```

`ARP-Spoof`: This attack works on layer 2 of the OSI model, specifically on the Address Resolution Protocol (ARP). It consists of sending an adulterated packet to the victim saying that we are the gateway of the local network, so the victim must send all its packets to our machine. We also tell the gateway that we are the victim; that way we become the man in the middle of the connection and can inspect all of the victims' packets with an analyzer.

```
...
├─── LAYER 2: ARP-SPOOF | DISCONNECT
├───┐
│   ├─── METHOD: ARP-SPOOF
│   │
│   ├─── [!] Scanning Local Network...
│   │
│   ├─── Avaliable Hosts:
│   │
│   │     192.168.0.102
│   │     192.168.0.105
│   │
│   ├─── IP: 192.168.0.102
│   ├─── TIME: 100
```

`Disconnect`: It blocks the victim from accessing the internet on the local network during the time the attack is happening.

```
...
├─── LAYER 2: ARP-SPOOF | DISCONNECT
├───┐
│   ├─── METHOD: DISCONNECT
│   │
│   ├─── [!] Scanning Local Network...
│   │
│   ├─── Avaliable Hosts:
│   │
│   │     192.168.0.100
│   │     192.168.0.103
│   │     192.168.0.105
│   │
│   ├─── IP: 192.168.0.100
│   ├─── TIME: 600
```

---
<br>

<div align="center">
  <h2>⚠ Tuyên bố từ chối trách nhiệm</h2><br>
</div>

This application is intended to be used as a testing tool against your own servers. **DO NOT USE IT TO ATTACK OTHER PEOPLE**, we don't take responsibility for anything that may come up if you attack someone else. Also, this project makes a `DoS` attack, if you want to take down well-hosted servers, then it's up to you to scale the attack using a `DDoS` approach. Know the limitations of what you can do, and the defense mechanism used by your target; for instance, if a webserver uses DDoS mitigation appliances (such as load balancing), then you'll probably fail to take it down; a router that implements SYN Cookies will not be affected by a SYN-Flood attack, and so on.
