Klasse ``RGB_LED`` - rgb LED
==============================

**Verwendung**

.. code-block:: python

    from robot_hat import PWM, RGB_LED

    r = PWM("P0")
    g = PWM("P1")
    b = PWM("P2")

    rgb = RGB_LED(r, g, b)                    # RGB_LED-Objekt erstellen
    val = rgb.write('#FFFFFF')                # Farbe in hexadezimaler Darstellung setzen.

**Konstruktoren**

``class robot_hat.RGB_LED(Rpin, Gpin, Bpin)``: Erstellt ein ``RGB_LED`` -Objekt, das mit den gegebenen Pins verknüpft ist. Dadurch können Sie die Farbe der RGB-LED einstellen. 
Die Eingabepins ``Rpin``, ``Gpin``, ``Bpin`` müssen ``PWM`` -Objekte aus ``robot_hat.PWM`` sein.

**Methoden**

-  ``write`` - Setzt eine spezifische Farbe für die RGB-LED. Der Farbwert wird in Hexadezimalzahlen für Rot, Grün und Blau (RGB) angegeben. Jede Farbe hat einen Minimalwert von 0 (00 in Hexadezimal) und einen Maximalwert von 255 (FF in Hexadezimal). Hexadezimale Werte werden mit einem # gefolgt von drei oder sechs Hexadezimalzeichen geschrieben.

.. code-block:: python

    RGB_LED.write(color)




