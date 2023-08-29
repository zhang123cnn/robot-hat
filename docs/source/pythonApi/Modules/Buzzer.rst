class ``Buzzer`` - パッシブブザー
=================================

**使用方法**

.. code-block:: python

    from robot_hat import PWM, Buzzer, Music

    pwm = PWM("A0")                           # PWMオブジェクトを生成
    buzzer = Buzzer(pwm)                      # PWMオブジェクトを使用してBuzzerオブジェクトを生成
    music = Music()                           # Musicオブジェクトを生成

    buzzer.play(music.note("Low C"), music.beat(1))  # ローCを1拍で演奏
    buzzer.play(music.note("Middle C#"))             # ミドルC#を演奏
    buzzer.off()                                     # ブザーをオフにする

**コンストラクタ**

``class robot_hat.Buzzer(pwm)``: 与えられたPWMオブジェクトに関連付けられたBuzzerオブジェクトを生成します。
これにより、ブザーを制御できます。

**メソッド**

-  ``on`` - ブザーを正方形波でオンにします。

.. code-block:: python

    Buzzer.on()

-  ``off`` - ブザーをオフにします。

.. code-block:: python

    Buzzer.off()

-  ``freq`` - 正方形波の周波数を設定します。

.. code-block:: python

    Buzzer.freq(frequency)

-  ``play`` - ブザーを特定の周波数で鳴らし、指定したミリ秒遅延時間で停止します。

.. code-block:: python

    Buzzer.play(freq, ms)
    Buzzer.play(freq)
