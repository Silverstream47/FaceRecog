import cv2

fase_cascade = cv2.CascadeClassifier("haarscascade_frontalface_alt.xml")

video = cv2.VideoCapture(0)

while True:
  _, frame = video.read()

  grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  detected_faces = face_cascade.detectMultiscale(grayscale)

  for (x, y, width, height) in detected_faces:
    cv2.rectangle(frame, (x,y) , (x + width, y + height), (0, 255, 0))

    cv2.imshow('Image', frame)

    if cv2.waitKey(1) == ord('q'):
      break

video.release
cv2.destroyAllWindows()