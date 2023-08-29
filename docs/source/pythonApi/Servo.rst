Klasse ``Servo`` - 3-Draht-PWM-Servotreiber
==============================================

**Verwendung**

.. code-block:: python

    from robot_hat import Servo, PWM

    pin = PWM("P0")
    ser = Servo(pin)                      # Ein Servo-Objekt erzeugen
    val = ser.angle(60)                   # Servowinkel einstellen

**Konstruktoren**

``class robot_hat.Servo(pin)``: Erzeugt ein Servo-Objekt, das mit dem angegebenen Pin assoziiert ist. Dadurch können Winkelwerte eingestellt werden.

**Methoden**

-  ``angle`` - Stellt die Winkelwerte zwischen -90 und 90 ein.

.. code-block:: python

    Servo.angle(90)