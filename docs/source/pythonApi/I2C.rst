.. _class_i2c:

Klasse ``i2c`` - IIC-Bus
=========================

**Verwendung**

.. code-block:: python

    from robot_hat import I2C

    i2c = I2C(1)                       # Erzeugt einen Bus auf Kanal 1
    i2c = I2C(1, I2C.MASTER)           # Erzeugt und initialisiert als Master

    i2c.send('abc')       # Sendet 3 Bytes
    i2c.send(0x42)        # Sendet ein einzelnes Byte, das durch die Nummer angegeben ist
    data = i2c.recv(3)    # Empfängt 3 Bytes

    i2c.is_ready(0x42)                 # Überprüft, ob der Slave 0x42 bereit ist
    i2c.scan()                         # Scannt den Bus nach Slaves, gibt eine Liste gültiger Adressen zurück
    i2c.mem_read(3, 0x42, 2)           # Liest 3 Bytes aus dem Speicher des Slaves 0x42, beginnend bei Adresse 2 im Slave
    i2c.mem_write('abc', 0x42, 2, timeout=1000)  # Schreibt 'abc' (3 Bytes) in den Speicher des Slaves 0x42, beginnend bei Adresse 2 im Slave, mit einer Timeout-Zeit von 1 Sekunde

**Konstruktoren**

``class robot_hat.I2C(num)``: Erstellt ein I2C-Objekt, das mit der angegebenen ``Nummer`` verknüpft ist. Dies ermöglicht Ihnen, I2C auf diesem Gerät zu verwenden.

**Methoden**

-  ``is_ready`` - Überprüft, ob der Slave 0x42 bereit ist.

.. code-block:: python

    I2C.is_ready(addr)

-  ``scan`` - Scannt den Bus nach Slaves und gibt eine Liste gültiger Adressen zurück.

.. code-block:: python

    I2C.scan()

-  ``send`` - Sendet mehrere Bytes an einen Slave mit einer bestimmten Adresse.

.. code-block:: python

    I2C.send(send,addr,timeout)

-  ``recv`` - Empfängt ein oder mehrere Bytes.

.. code-block:: python

    data = i2c.recv(recv,addr,timeout)  # Empfängt 3 Bytes

-  ``mem_write`` - Schreibt in den Speicher eines I2C-Geräts.

.. code-block:: python

    I2C.mem_write(data, addr, memaddr, timeout)

-  ``mem_read`` - Liest aus dem Speicher eines I2C-Geräts.

.. code-block:: python

    I2C.mem_read(data, addr, memaddr, timeout)

