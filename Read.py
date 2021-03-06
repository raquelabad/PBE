import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

class Rfid_Reader:
    
    def __init__(self):
        self.reader = SimpleMFRC522()
    def read_uid(self):
        id = self.reader.read_id()
        return (hex(id).upper()[2:10]) #retorna la part corresponent al uid en hexadecimal i majuscules

    
if __name__ =="__main__":
    try:
        rf=Rfid_Reader()
        uid = rf.read_uid()
        print(uid)
    finally:
        GPIO.cleanup()
