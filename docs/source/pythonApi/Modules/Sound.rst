class ``Sound`` - 音センサー
============================

**使用方法**

.. code-block:: python

    from robot_hat import Sound, ADC

    pin = ADC("A0")
    sound = Sound(pin)                       # ピンからSoundオブジェクトを生成
    val = sound.read_raw()                   # アナログ値を読む

    average_val = sound.read_raw(time = 100) # 平均アナログ値を読む

**コンストラクタ**

``class robot_hat.Sound(pin)``: 与えられたピンに関連付けられたSoundオブジェクトを生成します。このオブジェクトでピンのアナログ値を読むことができます。

**メソッド**

-  ``read_raw`` - アナログピンの値を読み取り、それを返します。返される値は0から4095の範囲になります。

.. code-block:: python

    Sound.read_raw()