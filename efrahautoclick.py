import ctypes

# Fare tıklama fonksiyonu
def click(x, y):
    ctypes.windll.user32.SetCursorPos(x, y)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)  # sol tık
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)  # sol tık bırak

# OpenCV tespitlerine göre fareyi hareket ettirme işlevi
def move_to_detected_location(x, y):
    # Algılanan nesnenin merkezine fareyi taşı
    click(x, y)
    # İsteğe bağlı olarak burada başka işlemler de yapabilirsiniz

# Örnek kullanım
if __name__ == "__main__":
    # OpenCV'den tespit edilen koordinatlar
    detected_x = 100
    detected_y = 100

    # Algılanan nesnenin koordinatlarına fareyi taşı
    move_to_detected_location(detected_x, detected_y)
