.. _class_adc:

Klasse ``ADC`` - Analog-Digital-Wandler
========================================

**Verwendung**

.. code-block:: python

    from robot_hat import ADC

    adc = ADC("A0")                    # Erzeugt ein Analogobjekt von einem Pin
    val = adc.read()                   # Liest Werte von analogen Pins

**Konstruktoren**

``class robot_hat.ADC(pin)``: Erstellt ein ADC-Objekt, das mit dem angegebenen Pin verknüpft ist. Dies ermöglicht Ihnen, analoge Werte an diesem Pin auszulesen.

**Methoden**

-  ``read`` - Liest den Wert am analogen Pin und gibt ihn zurück. Der zurückgegebene Wert liegt zwischen 0 und 4095.

.. code-block:: python

    ADC.read()


