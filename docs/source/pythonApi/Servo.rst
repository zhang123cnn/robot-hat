class ``Servo`` - 3線式PWMサーボドライバ
=========================================

**使用方法**

.. code-block:: python

    from robot_hat import Servo, PWM

    pin = PWM("P0")
    ser = Servo(pin)                    # サーボオブジェクトを作成
    val = ser.angle(60)                 # サーボの角度を設定

**コンストラクタ**

``class robot_hat.Servo(pin)``: 指定されたピンに関連付けられたサーボオブジェクトを作成。これにより、角度を設定できます。

**メソッド**

-  ``angle`` - 角度を-90から90の範囲で設定。

.. code-block:: python

    Servo.angle(90)
