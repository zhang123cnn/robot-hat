Klasse ``Buzzer`` - passiver Summer
=====================================

**Verwendung**

.. code-block:: python

    from robot_hat import PWM, Buzzer, Music

    pwm = PWM("A0")                          # Ein PWM-Objekt erzeugen
    buzzer = Buzzer(pwm)                     # Ein Buzzer-Objekt mit PWM-Objekt erzeugen
    music = Music()                          # Ein Musik-Objekt erzeugen

    buzzer.play(music.note("Low C"), music.beat(1))  # Tiefe C-Ton für 1 Schlag spielen
    buzzer.play(music.note("Middle C#"))             # Mittlere C# spielen
    buzzer.off()                                     # Summer ausschalten

**Konstruktoren**

``class robot_hat.Buzzer(pwm)``: Ein Buzzer-Objekt erzeugen, das mit dem gegebenen PWM-Objekt assoziiert ist. Dies ermöglicht die Steuerung des Buzzers.

**Methoden**

-  ``on`` - Schaltet den Buzzer mit einer Rechteckwelle ein.

.. code-block:: python

    Buzzer.on()

-  ``off`` - Schaltet den Buzzer aus.

.. code-block:: python

    Buzzer.off()

-  ``freq`` - Legt die Frequenz der Rechteckwelle fest.

.. code-block:: python

    Buzzer.freq(frequency)

-  ``play`` - Lässt den Buzzer mit einer bestimmten Frequenz erklingen und stoppt nach einer bestimmten Verzögerungszeit in Millisekunden.

.. code-block:: python

    Buzzer.play(freq, ms)
    Buzzer.play(freq)

