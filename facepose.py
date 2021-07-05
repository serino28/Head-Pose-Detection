import cv2

def camera():

    webcam = cv2.VideoCapture(0) #apertura della fotocamera
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #viene dato in pasto un xml che descrive come effettivamente è fatta una faccia

    while True:
       ret, frame = webcam.read() #catturiamo il nostro fotogramma, dove frame è il nostro fotogramma e ret è un valore booleano che ci indica se il fotogramma c'è o meno
       resized = cv2.resize(frame, None, fx=1, fy=1) #definizione ridimensionamento del frame
       faces = face_cascade.detectMultiScale(resized, 1.3, 5) #rileva un volto

       for (x,y,w,h) in faces: #se trovi un volto in ciò che si trova davanti alla fotocamera
           rettangolo = cv2.rectangle(resized, (x,y),(x+w,y+h),(0,255,0),2) #disegna un rettangolo
           centre_x = (x-w/2) #definizione coordinate utili per poter capire la posizione del volto riscontrato nello schermo
           if(rettangolo < centre_x).all():
               cv2.putText(resized, 'sei a sinistra', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2) #viceversa, 'sei a destra'
           elif(rettangolo > centre_x).all():
               cv2.putText(resized, 'sei al destra', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2) #viceversa, 'sei a destra'

       cv2.imshow('face pose', resized)
       if cv2.waitKey(1) & 0xFF == ord('q'): #premendo q si chiude la finestra
           break
    webcam.release() #rilascio della webcam
    cv2.destroyAllWindows() #distruzione della finestra


if __name__=='__main__':
    camera()