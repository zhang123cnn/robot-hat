class ``Ultrasonic`` - 超音波測距センサー
==========================================

**使用方法**

.. code-block:: python

    from robot_hat import Ultrasonic, Pin

    trig = Pin("D0")
    echo = Pin("D1")

    ultrasonic = Ultrasonic(trig, echo)       # Ultrasonicオブジェクトを生成
    val = ultrasonic.read()                   # アナログ値を読む

**コンストラクタ**

``class robot_hat.Ultrasonic(trig, echo)``: 与えられたピンに関連付けられたUltrasonicオブジェクトを生成します。このオブジェクトで距離の値を読むことができます。

**メソッド**

-  ``read`` - 距離の値を読む。

   .. code-block:: python

       Ultrasonic.read(trig, echo)