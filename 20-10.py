import tkinter as tk
import random

colors = [
    "#FFB6C1",  
    "#FF69B4",  
    "#FF1493",  
    "#DB7093",  
    "#C71585",  
    "#9370DB",  
    "#8A2BE2",  
    "#DA70D6",  
    "#DDA0DD",  
    "#E6E6FA",  
    "#F0E68C",  
]

messages = [
    "Loveeee You(Not today)",
    "Bạn là điều tuyệt vời nhất",
    "Mong bạn mãi vui vẻ nhó",
    "Bạn xứng đáng được hạnh phúc",
    "Hẹn ngày tui có được bạn",
    "Ghét m vcl coi chừng đó",
    "Chờ thêm 1 nhiều nữa nha",
    "Đừng trốn bn nữa bực lắm r",
    "Đừng tắt máy ấy, còn nhiều :v",
    "EEEEE Không biết viết gì nữa ấy :((",
    "Chúc bạn mãi xinh đẹp như này",
    "Mong không có chuyện buồn tìm đến",
    "Khong yeu em thi yeu ai >.<(sorry)",
    "Tầm này vẫn kịp mà, phải không?",
    "Nào thấy mệt, kể bn biết với -.-",
    "Nhớ ăn uống đầy đủ giữ gìn sức khỏe",
]


def random_color():
    return random.choice(colors)  
def get_contrast_color(bg_color):
    r = int(bg_color[1:3], 16)
    g = int(bg_color[3:5], 16)
    b = int(bg_color[5:7], 16)
    
    brightness = (r * 0.299 + g * 0.587 + b * 0.114)
    
    return "#000000" if brightness > 128 else "#FFFFFF"

def close_all_windows():
    for window in windows:
        window.destroy() 
    windows.clear()  

def show_congratulations_window():
    final_window = tk.Toplevel()  
    final_window.title("Yêu bạn")
    final_window.geometry("900x300")
    
    screen_width = final_window.winfo_screenwidth()
    screen_height = final_window.winfo_screenheight()
    x = (screen_width // 2) - (900 // 2)  
    y = (screen_height // 2) - (300 // 2)  
    final_window.geometry(f"900x300+{x}+{y}")  

    final_window.config(bg="#FFB6C1")  
    
    text_congratulations = (
        "Cảm ơn bạn đã chờ được đến đây! \n"
        "Chúc bạn một ngày 20/10 thật vui vẻ! <3 \n"
        "Chờ được 272 cửa sổ nhảy trong 30000ms rồi :v, \n"
        "thì thêm nhiều chút thời gian nữa có sao đâu ha??? \n"
        "Hẹn gặp vào dịp khác nha, m lủi kinh quá tìm k ra luôn rồi, \n"
        "lớn rồi, sn 18 lần 3 luôn r ấy. Đừng để bạn bực mình, ít nữa xuống nhà gô cổ về h :v ! \n"
        "Still here, still love you <3. Đừng để lộ ra ngoài, của nhà trồng được lộ ra ngại lắm :)))"
    )
    
    label = tk.Label(final_window, text=text_congratulations, font=("Arial", 14), fg="#4B0082", bg="#FFB6C1")
    label.pack(pady=20)

    close_button = tk.Button(final_window, text="Tắt đây nè", command=final_window.destroy)
    close_button.pack(pady=10)

def create_window(screen_width, screen_height):
    window = tk.Toplevel()  
    window.title("Chúc mừng ngày 20/10")
    window.geometry("320x80")
    
    x = random.randint(0, screen_width - 320)  
    y = random.randint(0, screen_height - 80)  
    
    window.geometry(f"320x80+{x}+{y}")  
    
    random_message = random.choice(messages)
    
    label = tk.Label(window, text=random_message, font=("Arial", 14))

    bg_color = random_color()  
    window.config(bg=bg_color)  

    label.config(fg=get_contrast_color(bg_color), bg=bg_color)  
    label.pack(pady=20)  

    return window

def create_window_with_delay(index, screen_width, screen_height):
    if index < 272:  
        window = create_window(screen_width, screen_height)
        windows.append(window)
        root.after(222, create_window_with_delay, index + 1, screen_width, screen_height)
    else:
        root.after(333, lambda: [close_all_windows(), show_congratulations_window()])  

windows = []

root = tk.Tk()
root.withdraw()  

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

create_window_with_delay(0, screen_width, screen_height)

root.mainloop()
