class ``ADXL345`` - 加速度計
===============================

**使用方法**

.. code-block:: python

    from robot_hat import ADXL345

    accel = ADXL345()                      # ADXL345オブジェクトを生成
    x_val = accel.read(accel.X)            # X軸（0）の値を読み取る
    y_val = accel.read(1)                  # Y軸（1）の値を読み取る
    z_val = accel.read(2)                  # Z軸（2）の値を読み取る

**コンストラクタ**

``class robot_hat.ADXL345(address=0x53)``: ADXL345オブジェクトを生成します。
これにより、adxl345の加速度値を読み取ることができます。

**メソッド**

-  ``read`` - 指定した軸の値を読み取り、それを返します。単位は重力加速度（約9.8m/s^2）です。

.. code-block:: python

    ADXL345.read(axis)

**定数**

-  ``X`` - x軸
-  ``Y`` - y軸
-  ``Z`` - z軸