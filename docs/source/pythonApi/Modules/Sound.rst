Klasse ``Sound`` - Schallsensor
===============================

**Verwendung**

.. code-block:: python

    from robot_hat import Sound, ADC

    pin = ADC("A0")
    sound = Sound(pin)                          # Schallsensor-Objekt aus einem Pin erstellen
    val = sound.read_raw()                      # Analogen Wert lesen

    average_val = sound.read_raw(time = 100)    # Durchschnittlichen analogen Wert lesen

**Konstruktoren**

``class robot_hat.Sound(pin)``: Erstellt ein Sound-Objekt, das mit dem gegebenen Pin verknüpft ist. Dadurch können Sie analoge Werte an diesem Pin auslesen.

**Methoden**

-  ``read_raw`` - Liest den Wert am analogen Pin und gibt ihn zurück. Der zurückgegebene Wert liegt zwischen 0 und 4095.

.. code-block:: python

    Sound.read_raw()