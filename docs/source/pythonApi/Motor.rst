.. _class_motor:

Klasse ``Motor`` - Motorsteuerung
=================================

**Verwendung**

.. code-block:: python

    from robot_hat import Motor

    motor = Motor()                      # Ein Motor-Objekt erzeugen
    motor = motor.wheel(100)             # Motorgeschwindigkeit auf 100 setzen

**Konstruktoren**

``class robot_hat.Motor()``: Erzeugt ein Motor-Objekt zur Steuerung der Motoren.

**Methoden**

-  ``wheel`` - Steuert Geschwindigkeit und Richtung des Motors.

.. code-block:: python

    # Der Geschwindigkeitsbereich liegt zwischen -100 und 100, wobei positive und negative Werte die Drehrichtung des Motors angeben.
    motor.wheel(100)

    # Der zweite Parameter, gefüllt mit 0 oder 1, dient zur Steuerung eines spezifischen Motors.
    motor.wheel(100, 1)