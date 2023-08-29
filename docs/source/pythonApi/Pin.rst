.. _class_pin:

Klasse ``Pin`` - Steuerung von I/O-Pins
===========================================

**Verwendung**

.. code-block:: python

    from robot_hat import Pin

    pin = Pin("D0")                     # Erzeugt ein Pin-Objekt von einem digitalen Pin
    val = pin.value()                   # Liest den Wert am digitalen Pin aus

    pin.value(0)                        # Setzt den digitalen Pin auf Low-Pegel

**Konstruktoren**

``class robot_hat.Pin(value)`` : ``Pin()`` ist das Basisobjekt zur Steuerung der I/O-Pins. Es bietet Methoden zur Einstellung des Pin-Modus (Eingang, Ausgang usw.) sowie zur Abfrage oder Festlegung des Pegels eines digitalen Pins.

**Methoden**

-  ``value`` - Liest oder setzt den Wert am digitalen Pin; der Wert ist 0/1.

.. code-block:: python

    Pin.value() # Ohne Parameter wird der GPIO-Pegel ausgelesen; hoher Pegel gibt 1 zurück, niedriger Pegel gibt 0 zurück.

    Pin.value(0)  # Setzt auf Low-Pegel    
    Pin.value(1)  # Setzt auf High-Pegel

-  Setzt den Wert am digitalen Pin, identisch mit ``value``.

.. code-block:: python

    Pin.on() # Setzt auf High-Pegel
    #off() # Setzt auf Low-Pegel
    #high() # Setzt auf High-Pegel
    #low() # Setzt auf Low-Pegel

-  ``mode`` - Setzt den Modus von GPIO auf ``IN`` oder ``OUT``.

.. code-block:: python
    
    Pin.mode(GPIO.IN)  # Setzt GPIO auf den EINGANG-Modus

**Verfügbare Pins**

-  ``"D0"``: Digitaler Pin 0.
-  ``"D1"``: Digitaler Pin 1.
-  ``"D2"``: Digitaler Pin 2.
-  ``"D3"``: Digitaler Pin 3.
-  ``"D4"``: Pin für den linken Motor.
-  ``"D5"``: Pin für den rechten Motor.
-  ``"D6"``
-  ``"D7"``
-  ``"D8"``
-  ``"D9"``
-  ``"SW"``: Die USR-Taste.
-  ``"LED"``: Die LED auf der Platine.


