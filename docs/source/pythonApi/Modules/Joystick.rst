class ``Joystick`` - 3軸ジョイスティック
========================================

**使用方法**

.. code-block:: python

    from robot_hat import Joystick, ADC, Pin

    x_pin = ADC("A0")
    y_pin = ADC("A1")
    btn_pin = Pin("D1")

    joystick = Joystick(x_pin, y_pin, btn_pin)    # ジョイスティックオブジェクトを生成
    val = joystick.read(0)                        # 軸の値を読む
    status = joystick.read_status()               # ジョイスティックの状態を読む

**コンストラクタ**

``class robot_hat.Joystick(pin)``: 与えられたピンに関連付けられたジョイスティックオブジェクトを生成します。これにより、ジョイスティックからの値を読むことができます。

**メソッド**

-  ``read`` - 指定されたピンの値を読み取り、それを返します。

.. code-block:: python

    Joystick.read(Xpin, Ypin, Btpin)

-  ``read_status`` - ジョイスティックの状態を読み取ります。

.. code-block:: python

    Joystick.read_status()

