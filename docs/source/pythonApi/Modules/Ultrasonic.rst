Klasse ``Ultrasonic`` - Ultraschall-Entfernungssensor
======================================================

**Verwendung**

.. code-block:: python

    from robot_hat import Ultrasonic, Pin

    trig = Pin("D0")
    echo = Pin("D1")

    ultrasonic = Ultrasonic(trig, echo)              # Erstellen eines Ultrasonic-Objekts
    val = ultrasonic.read()                          # Ein Analogwert auslesen

**Konstruktoren**

``class robot_hat.Ultrasonic(trig, echo)``: Erstellt ein Ultrasonic-Objekt, das mit den angegebenen Pins verknüpft ist. Dadurch ist es möglich, Entfernungsdaten auszulesen.

**Methoden**

-  ``read`` - Entfernungsdaten auslesen.

    .. code-block:: python

        Ultrasonic.read(trig, echo)




