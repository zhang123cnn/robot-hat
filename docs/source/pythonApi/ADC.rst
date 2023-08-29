.. _class_adc:

class ``ADC`` - アナログからデジタルへの変換器
==============================================

**使用方法**

.. code-block:: python

    from robot_hat import ADC

    adc = ADC("A0")                     # ピンからアナログオブジェクトを作成
    val = adc.read()                    # アナログピンから値を読み取る

**コンストラクタ**

``class robot_hat.ADC(pin)``: 指定されたピンに関連付けられたADCオブジェクトを作成します。これにより、そのピンでアナログ値を読むことができます。

**メソッド**

-  ``read`` - アナログピンの値を読み取り、返します。返される値は0から4095の間になります。

.. code-block:: python

    ADC.read()