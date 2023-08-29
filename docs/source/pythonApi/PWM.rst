.. _class_pwm:

class ``PWM`` - パルス幅変調
======================================

**使用方法**

.. code-block:: python

    from robot_hat import PWM

    pwm = PWM('P0')                      # ピンからPWMオブジェクトを作成
    PWM.freq(*freq)                      # 周波数（0-65535、単位はHz）
    PWM.prescaler(*prescaler)            # プリスケーラ
    PWM.period(*arr)  
    PWM.pulse_width(*pulse_width)        # パルス幅（pulse_width < period）
    PWM.pulse_width_percent(*pulse_width_percent)  # デューティーサイクル（0-100）

**コンストラクタ**

``class robot_hat.PWM(channel)``: 指定されたピンに関連付けられたPWMオブジェクトを作成します。これにより、そのピンでpwm機能を設定できます。

**メソッド**

-  ``freq`` - pwmチャンネルの周波数を設定します。

.. code-block:: python

    PWM.freq(50)

-  ``prescaler`` - pwmチャンネルのプリスケーラを設定します。

.. code-block:: python

    PWM.prescaler(50)

-  ``period`` - pwmチャンネルの周期を設定します。

.. code-block:: python

    PWM.period(100)

-  ``pulse_width`` - pwmチャンネルのパルス幅を設定します。

.. code-block:: python

    PWM.pulse_width(10)

-  ``pulse_width_percent`` - pwmチャンネルのパルス幅のパーセンテージを設定します。

.. code-block:: python

    PWM.pulse_width_percent(50)


