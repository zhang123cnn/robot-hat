Klasse ``ADXL345`` - Beschleunigungsmesser
=============================================

**Verwendung**

.. code-block:: python

    from robot_hat import ADXL345

    accel = ADXL345()                        # Ein ADXL345-Objekt erzeugen
    x_val = accel.read(accel.X)              # Einen X-Wert auslesen
    y_val = accel.read(1)                    # Einen Y-Wert auslesen
    z_val = accel.read(2)                    # Einen Z-Wert auslesen

**Konstruktoren**

``class robot_hat.ADXL345(address=0x53)``: Ein ADXL345-Objekt erzeugen. Damit können anschließend Beschleunigungswerte ausgelesen werden.

**Methoden**

-  ``read`` - Liest den Wert der jeweiligen Achse und gibt ihn zurück. Die Einheit ist die Erdbeschleunigung (etwa 9,8 m/s²).

.. code-block:: python

    ADXL345.read(axis)

**Konstanten**

-  ``X`` - X-Achse
-  ``Y`` - Y-Achse
-  ``Z`` - Z-Achse



