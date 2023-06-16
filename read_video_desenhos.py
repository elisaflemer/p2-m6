import cv2
import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Abre o arquivo de video
video_capture = cv2.VideoCapture("desenhos.mp4")

# Checa se foi possivel abrir o arquivo
if not video_capture.isOpened():
    print("Error opening video file")
    exit(1)

width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))  # float `width`
height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

output_video = cv2.VideoWriter(
    "out_desenhos.avi", cv2.VideoWriter_fourcc(*"DIVX"), 24, (width, height)
)


# Loop de leitura frame por frame
while True:
    # Le um frame do video e, guarda o resultado da leitura
    # Se nao houver mais frames disponiveis, ret sera falso
    ret, frame = video_capture.read()

    # Se nao conseguiu ler o frame, para o laco
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for x, y, w, h in faces:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y : y + h, x : x + w]
        roi_color = frame[y : y + h, x : x + w]
    if len(faces):
        output_video.write(frame)


    # Exibe o frame
    cv2.imshow("Video Playback", frame)

    # Se o usuario apertar q, encerra o playback
    # O valor utilizado no waiKey define o fps do playback
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

# Fecha tudo
output_video.release()
video_capture.release()
cv2.destroyAllWindows()
