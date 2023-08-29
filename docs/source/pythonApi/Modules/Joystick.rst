Klasse ``Joystick`` - 3-Achsen-Joystick
=======================================

**Verwendung**

.. code-block:: python

    from robot_hat import Joystick, ADC, Pin

    x_pin = ADC("A0")
    y_pin = ADC("A1")
    btn_pin = Pin("D1")

    joystick = Joystick(x_pin, y_pin, btn_pin)  # Joystick-Objekt erstellen
    val = joystick.read(0)                      # Achsenwert auslesen
    status = joystick.read_status()             # Joystick-Status auslesen

**Konstruktoren**

``class robot_hat.Joystick(pin)``: Erstellt ein Joystick-Objekt, das mit den angegebenen Pins verknüpft ist. Dies ermöglicht das Auslesen von Werten vom Joystick.

**Methoden**

-  ``read`` - Liest die Werte an den angegebenen Pins und gibt sie zurück.

.. code-block:: python

    Joystick.read(Xpin, Ypin, Btpin)

-  ``read_status`` - Liest den Status des Joysticks.

.. code-block:: python

    Joystick.read_status()

