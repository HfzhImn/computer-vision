import cv2, time

# Inisialisasi kamera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise RuntimeError("Kamera tidak bisa dibuka. Coba index 1/2.")

# Variabel untuk menghitung FPS
frames, t0 = 0, time.time()

while True:
    # Baca frame dari kamera
    ok, frame = cap.read()
    if not ok:
        break

    # Logika penghitung FPS
    frames += 1
    if time.time() - t0 >= 1.0:
        cv2.setWindowTitle("Preview", f"Preview (FPS ~ {frames})")
        frames, t0 = 0, time.time()

    # Tampilkan frame di jendela
    cv2.imshow("Preview", frame)

    # Berhenti jika tombol 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Lepaskan kamera dan tutup semua jendela
cap.release()
cv2.destroyAllWindows()