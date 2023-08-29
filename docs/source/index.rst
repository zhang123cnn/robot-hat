SunFounder ロボット HAT
=====================================

ロボット HAT は、Raspberry Pi を短時間でロボットに変換できる多機能拡張ボードです。搭載されている MCU により、Raspberry Pi の PWM 出力と ADC 入力を拡張し、モータードライバチップ、Bluetooth モジュール、I2S オーディオモジュール、モノラルスピーカーも内蔵しています。さらに、Raspberry Pi 自体から引き出される GPIO も利用可能です。

このボードにはスピーカーも付属しており、バックグラウンドミュージックや効果音を再生するだけでなく、TTS 機能を実装してプロジェクトをより魅力的にすることができます。

7-12V PH2.0 2ピン電源入力に対応し、2つの電源インジケーターがあります。また、効果をすぐにテストできるように、ユーザー用の LED とボタンも搭載されています。

このドキュメントでは、SunFounder が提供する Python ``robot-hat`` ライブラリを通じて、ロボット HAT のインターフェース機能とその使用方法について詳しく解説します。

.. .. image:: img/robot_hat.jpg
..    :width: 400
..    :align: center
.. 新しい写真待ち


.. toctree::
   :maxdepth: 3

   hardware_introduction
   installation
   api
   faq
