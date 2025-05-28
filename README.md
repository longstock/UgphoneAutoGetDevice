# UgphoneAutoGetDevice
Tool python tự động lấy ugphone trial 4h, no key, sẽ update sau
- Phiên bản không có proxy, cần bật vpn để sử dụng là ugv1.py
- Phiên bản đã có proxy tích hợp và không cần bật vpn là ugv2.py (khuyến khích sử dụng)
code open source nên thoải mái check, ko có virus đâu
# 1. Hướng dẫn sử dụng cho người ko biết dùng:

B1: Tải Python phiên bản mới nhất ở trang https://www.python.org/downloads/

B2: Mở file lên xog cài đặt mặc định

B3: mở cmd/powershell, run code:
```
pip install -r requirements.txt
```
b4 (bước này chỉ dành cho ugv1): lên gg search proton vpn xog r tải bản free về, đăng nhập xog r ấn quick connect đến một nước bất kì, có premium thì chọn server Japan (thật ra server nước nào chả đc) là tốt nhất, bật xog thì trong cmd/powershell gõ:
```
cd [vị trí folder chứa file]
```
B5: sau đó chọn phiên bản muốn dùng (khuyến khích ugv2.py)
dành cho v1:
```
python ugv1.py
```
dành cho v2:
```
python ugv2.py
```
Các lỗi thường gặp: (chỉ dành cho ugv2)
- Nếu code báo đã tìm ra proxy nhưng sau đó lại lỗi và kết thúc thì có nghĩa rằng đã hết proxy hoặc không hoạt động, chờ 5 phút sau đó thử lại (vì đây là proxy free nên hoàn toàn có giới hạn)
- Bắt buộc cần nhập đúng UgPhone Local storage để tránh bị lỗi
khó hiểu chỗ nào thì dm discord, username t là withstock


