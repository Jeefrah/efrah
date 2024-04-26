import ctypes

# Fare tıklama fonksiyonu
def click(x, y):
    ctypes.windll.user32.SetCursorPos(x, y)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)  # sol tık
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)  # sol tık bırak

# Fareyi belirli bir konuma taşıma işlevi
def move(x, y):
    ctypes.windll.user32.SetCursorPos(x, y)

# Örnek kullanım
if __name__ == "__main__":
    # OpenCV'den tespit edilen koordinatlar
    detected_x = 100
    detected_y = 100

    # Algılanan nesnenin koordinatlarına fareyi taşı
    move(detected_x, detected_y)
    # Tıklama işlemi
    click(detected_x, detected_y)
