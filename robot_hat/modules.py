#!/usr/bin/env python3
from .pin import Pin
from .pwm import PWM
from .adc import ADC
from .i2c import I2C
import time


class Ultrasonic():
    """UltraSonic modules"""

    def __init__(self, trig, echo, timeout=0.02):
        """
        Initialize the ultrasonic class

        :param trig: trig pin
        :type trig: robot_hat.Pin
        :param echo: echo pin
        :type echo: robot_hat.Pin
        :param timeout: timeout in seconds
        :type timeout: float
        :raise ValueError: if trig or echo is not a Pin object
        """
        if not isinstance(trig, Pin):
            raise TypeError("trig must be robot_hat.Pin object")
        if not isinstance(echo, Pin):
            raise TypeError("echo must be robot_hat.Pin object")
        self.trig = trig
        self.echo = echo
        self.timeout = timeout

    def _read(self):
        self.trig.low()
        time.sleep(0.01)
        self.trig.high()
        time.sleep(0.00001)
        self.trig.low()
        pulse_end = 0
        pulse_start = 0
        timeout_start = time.time()
        while self.echo.value() == 0:
            pulse_start = time.time()
            if pulse_start - timeout_start > self.timeout:
                return -1
        while self.echo.value() == 1:
            pulse_end = time.time()
            if pulse_end - timeout_start > self.timeout:
                return -1
        during = pulse_end - pulse_start
        cm = round(during * 340 / 2 * 100, 2)
        return cm

    def read(self, times=10):
        """
        Read distance in cm

        :param times: times try to read
        :type times: int
        :return: distance in cm, -1 if timeout
        :rtype: float
        """
        for _ in range(times):
            a = self._read()
            if a != -1:
                return a
        return -1


class ADXL345():
    """ADXL345 modules"""

    X = 0
    """X"""
    Y = 1
    """Y"""
    Z = 2
    """Z"""

    _REG_DATA_X = 0x32  # X-axis data 0 (6 bytes for X/Y/Z)
    _REG_DATA_Y = 0x34  # Y-axis data 0 (6 bytes for X/Y/Z)
    _REG_DATA_Z = 0x36  # Z-axis data 0 (6 bytes for X/Y/Z)
    _REG_POWER_CTL = 0x2D  # Power-saving features control
    _AXISES = [_REG_DATA_X, _REG_DATA_Y, _REG_DATA_Z]

    def __init__(self, address=0x53):
        """
        Initialize ADXL345

        :param address: address of the ADXL345
        :type address: int
        """
        self.i2c = I2C(address=address)
        self.address = address

    def read(self, axis):
        """
        Read an axis from ADXL345

        :param axis: axis to read, ADXL345.X, ADXL345.Y or ADXL345.Z
        :type axis: int
        :return: value of the axis
        :rtype: int
        """
        raw_2 = 0
        result = self.i2c.read()
        data = (0x08 << 8) + self._REG_POWER_CTL
        if result:
            self.i2c.write(data)
        self.i2c.mem_write(0, 0x31)
        self.i2c.mem_write(8, 0x2D)
        raw = self.i2c.mem_read(2, self._AXISES[axis])
        # 第一次读的值总是为0，所以多读取一次
        self.i2c.mem_write(0, 0x31)
        self.i2c.mem_write(8, 0x2D)
        raw = self.i2c.mem_read(2, self._AXISES[axis])
        if raw[1] >> 7 == 1:

            raw_1 = raw[1] ^ 128 ^ 127
            raw_2 = (raw_1 + 1) * -1
        else:
            raw_2 = raw[1]
        g = raw_2 << 8 | raw[0]
        value = g / 256.0
        return value


class RGB_LED():
    """Simple 3 pin RGB LED"""

    ANODE = 1
    """Common anode"""
    CATHODE = 0
    """Common cathode"""

    def __init__(self, r_pin, g_pin, b_pin, common=1):
        """
        Initialize RGB LED

        :param r_pin: PWM object for red
        :type r_pin: robot_hat.PWM
        :param g_pin: PWM object for green
        :type g_pin: robot_hat.PWM
        :param b_pin: PWM object for blue
        :type b_pin: robot_hat.PWM
        :param common: RGB_LED.ANODE or RGB_LED.CATHODE, default is ANODE
        :type common: int
        :raise ValueError: if common is not ANODE or CATHODE
        :raise TypeError: if r_pin, g_pin or b_pin is not PWM object
        """
        if not isinstance(r_pin, PWM):
            raise TypeError("r_pin must be robot_hat.PWM object")
        if not isinstance(g_pin, PWM):
            raise TypeError("g_pin must be robot_hat.PWM object")
        if not isinstance(b_pin, PWM):
            raise TypeError("b_pin must be robot_hat.PWM object")
        if common not in (self.ANODE, self.CATHODE):
            raise ValueError("common must be RGB_LED.ANODE or RGB_LED.CATHODE")
        self.r_pin = r_pin
        self.g_pin = g_pin
        self.b_pin = b_pin
        self.common = common

    def write(self, color):
        """
        Write color to RGB LED

        :param color: color to write, hex string starts with "#", 24-bit int or tuple of (red, green, blue)
        :type color: str/int/tuple
        """
        if not isinstance(color, (str, int, tuple, list)):
            raise TypeError("color must be str, int, tuple or list")
        if isinstance(color, str):
            color = color.strip("#")
            color = int(color, 16)
        if isinstance(color, (tuple, list)):
            r, g, b = color
        if isinstance(color, int):
            r = (color & 0xff0000) >> 16
            g = (color & 0x00ff00) >> 8
            b = (color & 0x0000ff) >> 0

        if self.common == self.ANODE:
            r = 255-r
            g = 255-g
            b = 255-b

        r = r / 255.0 * 100.0
        g = g / 255.0 * 100.0
        b = b / 255.0 * 100.0

        self.r_pin.pulse_width_percent(r)
        self.g_pin.pulse_width_percent(g)
        self.b_pin.pulse_width_percent(b)


class Buzzer():
    """Buzzer"""

    def __init__(self, buzzer):
        """
        Initialize buzzer

        :param pwm: PWM object for passive buzzer or Pin object for active buzzer
        :type pwm: robot_hat.PWM/robot_hat.Pin
        """
        if not isinstance(buzzer, (PWM, Pin)):
            raise TypeError(
                "buzzer must be robot_hat.PWM or robot_hat.Pin object")
        self.buzzer = buzzer

    def on(self):
        """Turn on buzzer"""
        if isinstance(self.buzzer, PWM):
            self.buzzer.pulse_width_percent(50)
        elif isinstance(self.buzzer, Pin):
            self.buzzer.on()

    def off(self):
        """Turn off buzzer"""
        if isinstance(self.buzzer, PWM):
            self.buzzer.pulse_width_percent(0)
        elif isinstance(self.buzzer, Pin):
            self.buzzer.off()

    def freq(self, freq):
        """Set frequency of passive buzzer

        :param freq: frequency of buzzer, use Music.NOTES to get frequency of note
        :type freq: int/float
        :raise TypeError: if set to active buzzer
        """
        if isinstance(self.buzzer, Pin):
            raise TypeError("freq is not supported for active buzzer")
        self.buzzer.freq(freq)

    def play(self, freq, duration=None):
        """
        Play notes

        :param args: notes to play, see play_note for details
        :type args: str/int/float
        :param duration: duration of each note, in ms, None means play continuously
        :type duration: float
        :raise TypeError: if set to active buzzer
        """
        if isinstance(self.buzzer, Pin):
            raise TypeError("play is not supported for active buzzer")
        self.freq(freq)
        self.on()
        if duration is not None:
            time.sleep(duration/1000.0)
            self.off()
            time.sleep(duration/1000.0)


class Sound():
    """Sound sensor"""

    def __init__(self, adc):
        """
        Initialize sound sensor

        :param adc: ADC object for sound sensor
        :type adc: robot_hat.ADC
        :raise TypeError: if adc is not ADC object
        """
        if not isinstance(adc, ADC):
            raise TypeError("adc must be robot_hat.ADC object")
        self.sensor = adc

    def read_raw(self):
        """Read raw value of sound sensor"""
        return self.sensor.read()

    def read(self, times=50):
        """
        Read value of sound sensor

        :param times: times to average
        :type times: int
        :return: average value of sound sensor
        :rtype: float
        """
        value_list = []
        for _ in range(times):
            value = self.read_raw()
            value_list.append(value)
        value = sum(value_list)/times
        return value


class Grayscale_Module(object):
    """3 channel Grayscale Module"""

    def __init__(self, pin0, pin1, pin2, reference=1000):
        """
        Initialize Grayscale Module

        :param pin0: ADC object or int for channel 0
        :type pin0: robot_hat.ADC/int
        :param pin1: ADC object or int for channel 1
        :type pin1: robot_hat.ADC/int
        :param pin2: ADC object or int for channel 2
        :type pin2: robot_hat.ADC/int
        :param reference: reference voltage
        :type reference: int
        """
        if isinstance(pin0, ADC):
            self.chn_0 = pin0
        else:
            self.chn_0 = ADC(pin0)
        if isinstance(pin1, ADC):
            self.chn_1 = pin1
        else:
            self.chn_1 = ADC(pin1)
        if isinstance(pin2, ADC):
            self.chn_2 = pin2
        else:
            self.chn_2 = ADC(pin2)
        self.reference = reference

    def get_line_status(self, data):
        """
        Get line status

        :param data: list of grayscale data
        :type data: list
        :return: line status, stop, forward, backward, left, right
        :rtype: str
        """
        if data[0] > self.reference and data[1] > self.reference and data[2] > self.reference:
            return 'stop'

        elif data[1] <= self.reference:
            return 'forward'

        elif data[0] <= self.reference:
            return 'right'

        elif data[2] <= self.reference:
            return 'left'

    def get_grayscale_data(self):
        """
        Get grayscale data

        :return: list of grayscale data
        :rtype: list
        """
        adc_value_list = []
        adc_value_list.append(self.chn_0.read())
        adc_value_list.append(self.chn_1.read())
        adc_value_list.append(self.chn_2.read())
        return adc_value_list
