import tkinter as tk
from tkinter import ttk
import socket


def check_ports(host, ports):
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports


def scan_ports():
    host = entry_host.get()
    port_range = entry_ports.get()

    try:
        start, end = map(int, port_range.split('-'))
        ports_to_scan = range(start, end + 1)
    except ValueError:
        result_label.config(text="Некорректный диапазон портов.")
        return

    open_ports = check_ports(host, ports_to_scan)

    if open_ports:
        result_label.config(text=f"Открытые порты: {', '.join(map(str, open_ports))}")
    else:
        result_label.config(text="Все порты в указанном диапазоне закрыты.")


# Создаем основное окно
root = tk.Tk()
root.title("Сканер портов")

# Создаем и размещаем элементы интерфейса
label_host = ttk.Label(root, text="Хост:")
label_host.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

entry_host = ttk.Entry(root)
entry_host.grid(row=0, column=1, padx=10, pady=10)

label_ports = ttk.Label(root, text="Диапазон портов (например, 80-100):")
label_ports.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

entry_ports = ttk.Entry(root)
entry_ports.grid(row=1, column=1, padx=10, pady=10)

scan_button = ttk.Button(root, text="Сканировать порты", command=scan_ports)
scan_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label = ttk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Запускаем главный цикл
root.mainloop()
