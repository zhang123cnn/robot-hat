Hardware Introduction
=========================

.. .. image:: img/picar_x_pic7.png

.. **Motor Port**
..     * 2-channel XH2.54 motor ports.
..     * The motor port 1 is connected to GPIO 23 and the motor port 2 is connected to GPIO 24.
..     * API: :ref:`class_motor`, ``0`` for left motor port, ``1`` for right motor port.

.. **I2C Pin**
..     * 2-channel I2C pins from Raspberry Pi.
..     * API: :ref:`class_i2c`

.. **PWM Pin**
..     * 12-channel PWM pins, P0-P12.
..     * API: :ref:`class_pwm`

.. **ADC Pin**
..     * 4-channel ADC pins, A0-A3.
..     * API: :ref:`class_adc`

.. **Digital Pin**
..     * 4-channel digital pins, D0-D3.
..     * API: :ref:`class_pin`

.. **Battery Indicator**
..     * Two LEDs light up when the voltage is higher than 7.8V.
..     * One LED lights up in the 6.7V to 7.8V range. 
..     * Below 6.7V, both LEDs turn off.

.. **LED**
..     * Set by your program. (Outputting 1 turns the LED on; Outputting 0 turns it off.)
..     * API: :ref:`class_pin`, you can use ``Pin("LED")`` to define it.

.. **RST Button**
..     * Short pressing RST Button causes program resetting.
..     * Long press RST Button till the LED lights up then release, and you will disconnect the Bluetooth.

.. **USR Button**
..     * The functions of USR Button can be set by your programming. (Pressing down leads to a input “0”; releasing produces a input “1”. ) 
..     * API: :ref:`class_pin`, you can use ``Pin("SW")`` to define it.

.. **Power Switch**
..     * Turn on/off the power of the robot HAT.
..     * When you connect power to the power port, the Raspberry Pi will boot up. However, you will need to switch the power switch to ON to enable Robot HAT.

.. **Power Port**
..     * 7-12V PH2.0 2pin power input.
..     * Powering the Raspberry Pi and Robot HAT at the same time.

.. **Bluetooth Module**
..     * Since the Raspberry Pi comes with Bluetooth in slave mode, there will be pairing problems when connecting with cell phones. To make it easier for the Raspberry Pi to connect to the Ezblock Studio, we added a separate Bluetooth module.
..     * Ezblock Studio is a custom graphical programming application developed by SunFounder for Raspberry Pi, for more information please refer to: `Ezblock Studio 3 <https://docs.sunfounder.com/projects/ezblock3/en/latest/>`_.


.. **Bluetooth Indicator**
..     * The Bluetooth indicator keeps turning on at a well Bluetooth connection, blink at a Bluetooth disconnection, blink fast at a signal transmission.    

The Robot Hat V4 features 2 lithium battery charging, 5V/3A DC-DC discharge, I2S audio output and speaker, a simple battery level indicator, microcontroller-based PWM and ADC drivers, as well as motor drivers.


Features:
    * Shutdown Current: < 0.5mA
    * Power Input: USB Type-C, 5V/2A
    * Charging Power: 5V/2A 10W
    * Output Power: 5V/3A
    * Included Batteries: 2 x 3.7V 18650 Lithium-ion Batteries, XH2.0 3P Interface
    * Battery Protection: Reverse polarity protection
    * Charging Protection: Input undervoltage protection, input overvoltage protection, charging balance, overheat protection
    * Onboard Charging Indicator Light: CHG
    * Onboard Power Indicator Light: PWR
    * Onboard 2 Battery Level Indicator LEDs
    * Onboard User LED, 2 tactile switches
    * Motor Driver: 5V/1.8A x 2
    * 4-channel 12-bit ADC
    * 12-channel PWM
    * 4-channel digital signals
    * Onboard SPI interface, UART interface, I2C interface
    * Mono Speaker: 8Ω1W

.. list-table:: Electrical Characteristics
   :widths: 50 25 25 25 25
   :header-rows: 1

   * - Parameters:
     - Minimum Value:
     - Typical Value:
     - Maximum Value:
     - Unit:
   * - Input Voltage:
     - 4.25
     - 5
     - 8.4
     - V
   * - Battery Input Voltage:
     - 6.0
     - 7.4
     - 8.4
     - V
   * - Overcharge Protection (Battery):
     -
     - 8.3
     -
     - V
   * - Input Undervoltage Protection:
     - 4.15
     - 4.25
     - 4.35
     - V
   * - Input Overvoltage Protection:
     - 8.3
     - 8.4
     - 8.5
     - V
   * - Charging Current (5V):
     -
     -
     - 2.0
     - A
   * - Output Current (5V):
     -
     -
     - 3.0
     - A
   * - Output Voltage:
     - 5.166
     - 5.246
     - 5.327
     - V
   * - Charging Overheat Protection:
     - 125
     - 135
     - 145
     - °C
   * - DC-DC Overheat Protection:
     - 70
     - 75
     - 80
     - °C
   * - Motor Output Current:  
     -
     -
     - 1.8
     - A  


Details
----------------

**Pin & GPIO**

.. list-table:: Raspberry Pi IO
    :widths: 50 50 50 50
    :header-rows: 1

    * - Robot Hat V4
      - Raspberry Pi 
      - Robot Hat V4
      - Raspberry Pi
    * - NC
      - 3V3    
      - 5V
      - 5V
    * - SDA
      - SDA    
      - 5V
      - 5V
    * - SCL
      - SCL    
      - GND
      - GND
    * - D1
      - GPIO4    
      - TXD
      - TXD
    * - GND
      - GND    
      - RXD
      - RXD
    * - D0
      - GPIO17    
      - I2S BCLK
      - GPIO18
    * - D2
      - GPIO27    
      - GND
      - GND
    * - D3
      - GPIO22    
      - MOTOR 1 DIR
      - GPIO23
    * - NC
      - 3V3    
      - MOTOR 2 DIR
      - GPIO24
    * - SPI MOSI
      - MOSI    
      - GND
      - GND
    * - SPI MISO
      - MISO    
      - USR BUTTON
      - GPIO25
    * - SPI SCLK
      - SCLK    
      - SPI CE0
      - CE0
    * - GND
      - GND    
      - NC
      - CE1
    * - NC
      - ID_SD    
      - NC
      - ID_SC
    * - MCU Reset
      - GPIO5    
      - GND
      - GND
    * - (SPI)BSY 
      - GPIO6    
      - Board Identifier 2
      - GPIO12
    * - Board Identifier 1
      - GPIO13    
      - GND
      - GND
    * - I2S LRCLK
      - GPIO19    
      - RST BUTTON
      - GPIO16
    * - USER LED
      - GPIO26    
      - NC
      - GPIO20
    * - GND
      - GND    
      - I2S SDATA
      - GPIO21


**Digital IO**
    
Robot HAT has 4 sets of 3Pin digital pins of P2.54.

.. image:: img/digitalio.png

.. list-table:: Digital IO
    :widths: 25 50
    :header-rows: 1

    * - Robot Hat V4
      - Raspberry Pi 

    * - D0
      - GPIO17

    * - D1
      - GPIO4

    * - D2
      - GPIO27

    * - D3
      - GPIO22


**ADC**

.. image:: img/adcpin.png

Robot HAT has 4 sets of 3Pin ADC pins of P2.54, and the power supply is 3.3V.
The ADC (Analog to Digital Converter) is provided by a microcontroller with 12-bit precision. 
The method of reading the ADC value is described in detail in `Onboard microcontroller`.

.. image:: img/btradc.png

Also, ADC channel A4 is connected to the battery through a voltage divider using resistors, 
which will be used to measure the battery voltage to estimate the approximate battery charge.

The voltage divider ratio is 20K/10K, so:
A4 voltage (Va4) = value_A4 / 4095.0 * 3.3
Battery voltage (Vbat) = Va4*3
Battery voltage (Vbat) = value_A4 / 4095.0 * 3.3 * 3

**PWM**

.. image:: img/pwmpin.png

Robot HAT has 4 sets of 3Pin ADC pins of P2.54, and the power supply is 5V.
The method of using the PWM is described in detail in `Onboard microcontroller`.

.. note:: PWM13 & 14 channels are used for motor drive.

**I2C**

.. image:: img/i2cpin.png

The Robot HAT has two I2C interfaces. One is the P2.54 4-pin interface, and the other is the SH1.0 4-pin interface, which is compatible with QWIIC and STEMMA QT. 
These I2C interfaces are connected to the Raspberry Pi's I2C interface via GPIO2 (SDA) and GPIO3 (SCL). 
The board also features an `onboard microcontroller`, and the two signal lines have 10K pull-up resistors.

**SPI**

.. image:: img/spipin.png

The SPI interface of the Robot HAT is a 7-pin P2.54 interface. 
It connects to the SPI interface of the Raspberry Pi and includes an additional I/O pin that can be used for purposes such as interrupts or resets.


.. list-table:: SPI
    :widths: 50 50
    :header-rows: 1

    * - Robot Hat V4
      - Raspberry Pi 
    * - BSY
      - GPIO6
    * - CS
      - CE0(GPIO8)
    * - SCK
      - SCLK(GPIO11)
    * - MI
      - MISO(GPIO9)
    * - MO
      - MOSI(GPIO10)
    * - 3V3
      - 3.3V Power
    * - GND
      - Ground


**UART**

.. image:: img/uartpin.png

The UART interface of the Robot HAT is a 4-pin P2.54 interface. It connects to the Raspberry Pi's GPIO14 (TXD) and GPIO15 (RXD) pins.


**LED & Button**

The Robot HAT comes with 1 LED and 2 buttons, all directly connected to the Raspberry Pi's GPIO pins. 
The RST button, when using Ezblock, serves as a button to restart the Ezblock program. 
If not using Ezblock, the RST button does not have a predefined function and can be fully customized according to your needs.

.. list-table:: LED & Button
    :widths: 50 50
    :header-rows: 1

    * - Robot Hat V4
      - Raspberry Pi 
    * - LED
      - GPIO26
    * - USR
      - GPIO25
    * - RST
      - GPIO16


**I2S Audio**

The Robot HAT is equipped with onboard I2S audio output, along with a 2030 audio chamber speaker, providing a mono sound output.


.. list-table:: I2S
    :widths: 50 50
    :header-rows: 1

    * - I2S
      - Raspberry Pi
    * - LRCLK
      - GPIO19
    * - BCLK
      - GPIO18
    * - SDATA
      - GPIO21


**Motor Driver**

The motor driver of the Robot HAT supports 2 channels and can be controlled using 2 digital signals for direction and 2 PWM signals for speed control.


.. list-table:: Motor Driver
    :widths: 50 50
    :header-rows: 1

    * - Motor
      - IO
    * - Motor1 Dir
      - GPIO23
    * - Motor1 Power
      - PWM13
    * - Motor2 Dir
      - GPIO24
    * - Motor2 Power
      - PWM12

**Charging Balancing**

When any one of the batteries reaches or exceeds 4.1V while the others are below that threshold, 
the charging current of that specific battery will be reduced.


**Battery Level Indicator**

The battery level indicator on the Robot HAT monitors the battery voltage using a voltage divider method and serves as a reference for estimating the battery level. 
The relationship between the LED and voltage is as follows:

.. list-table:: Battery Level
    :widths: 50 50
    :header-rows: 1

    * - LED Battery
      - Total Voltage
    * - 2 LEDs on
      - Greater than 7.6V
    * - 1 LED on
      - Greater than 7.15V
    * - Both LEDs off
      - Less than 7.15V

  
**Battery**

.. image:: img/battery.png

The product is equipped with two series-connected 3.7V 18650 lithium-ion batteries with a nominal capacity of 2000mAh. 
The batteries are connected using an XH2.54 3-pin interface.

* Composition: Li-ion (Lithium-ion)
* Capacity: 2000mAh, 14.8Wh
* Weight: 90.8g
* Number of Cells: 2
* Connector: XH2.54 3P
* Over-discharge Protection: 6.0V

**Onboard Microcontroller**

The Robot HAT comes with an AT32F415CBT7 microcontroller from Artery. 
It is an ARM Cortex-M4 processor with a maximum clock frequency of 150MHz. 
The microcontroller has 256KB of Flash memory and 32KB of SRAM.

The onboard PWM and ADC are driven by the microcontroller. 
Communication between the Raspberry Pi and the microcontroller is established via the I2C interface. 
The I2C address used for communication is 0x14 (7-bit address format).

Register:

ADC Read Value (0x10-0x17) 
  Reads the value of the ADC. Data is read back in 16-bit format [MSB], [LSB].
  0x17: ADC 0
  0x16: ADC 1
  ...
  0x13: ADC 4
  0x12: ADC 5 (Reserved)
  0x11: ADC 6 (Reserved)
  0x10: ADC 7 (Reserved)

PWM Pulse Width (0x20-0x2D) 
  Sets the PWM pulse width. Data is written in 16-bit format [MSB], [LSB].
  0x20: PWM 0
  0x21: PWM 1
  ...
  0x2B: PWM 11
  0x2C: PWM 12 (Motor)
  0x2D: PWM 13 (Motor)

PWM Prescaler (0x40-0x43) 
  Sets the prescaler for PWM. Data is written in 16-bit format [MSB], [LSB].
  0x40: PWM Channel 0
  0x41: PWM Channel 1
  0x42: PWM Channel 2
  0x43: PWM Channel 3

PWM Period (0x44-0x47) 
  Sets the period of the PWM. Data is written in 16-bit format [MSB], [LSB].
  0x44: PWM Channel 0
  0x45: PWM Channel 1
  0x46: PWM Channel 2
  0x47: PWM Channel 3

**PWM Frequency and Period Setting**

The PWM frequency is determined by the period (Period) and the prescaler (ARR). The principle is based on an internal clock of the microcontroller running at 72MHz. By dividing the clock with the prescaler, we obtain a frequency (Fp). Then, by dividing Fp with the period, we can calculate the desired frequency (F). Therefore:

F = 72000000 / ARR / Period

In general, we determine the frequency and period to calculate the prescaler. For example, if you need to drive a servo motor with a frequency of 50Hz and a precision of 12 bits (period of 2^12, which is 4096), you can calculate the prescaler (ARR) as follows:

ARR = 72000000 / F * Period
= 72000000 / 50 / 4096
= 351.6525
≈ 352

Since ARR needs to be an integer, it will be rounded to 352. Therefore, you can set ARR as 352 and Period as 4096 to achieve an actual PWM frequency of approximately 49.937Hz, which is close to 50Hz.

The default values for the PWM prescaler (ARR) and period (Period) are 352 and 4096, respectively, resulting in a default frequency of 50Hz.

**PWM Pulse Width**

The pulse width corresponds to the number of periods. For example, if the period (Period) is set to 4096, 
and you set the pulse width value to 2048, you will achieve a 50% PWM output.