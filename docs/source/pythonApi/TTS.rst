class ``TTS`` - テキストから音声へ
===================================

**使用方法**

.. code-block:: python

       from robot_hat import *

       tts = TTS()                    # TTSオブジェクトを作成
       tts.say('hello')               # 単語を発音

       # tts.write('hi')              # 単語を発音
       tts.lang('en-GB')              # 言語を変更

       tts.supported_lang()           # サポートされている言語を取得

**コンストラクタ**

``class robot_hat.TTS(engine)``: TTSオブジェクトを作成。 ``engine`` には ``"espeak"`` をEspeak、 ``"gtts"`` をGoogle TTS、 ``"polly"`` をAWS Pollyとして指定できます。

**メソッド**

-  ``say`` - TTSで単語を発音。

.. code-block:: python

       TTS.say(words)

-  ``lang`` - TTSでの言語を変更。

.. code-block:: python

       TTS.lang(language)

-  ``supported_lang`` - サポートされている全言語を照会。

.. code-block:: python

       TTS.supported_lang()

-  パラメータ調整

.. code-block:: python

       # amp: 振幅、音量
       # speed: 語速
       # gap: 間隔
       # pitch: ピッチ
       def espeak_params(self, amp=None, speed=None, gap=None, pitch=None)
