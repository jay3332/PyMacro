def linear(n):
    if not 0.0 <= n <= 1.0:
        raise ValueError("Argument must be between 0.0 and 1.0.")
    return n

from pytweening import (
    easeInQuad as ease_in_quad,
    easeOutQuad as ease_out_quad,
    easeInOutQuad as ease_in_out_quad,
    easeInCubic as ease_in_cubic,
    easeOutCubic as ease_out_cubic,
    easeInOutCubic as ease_in_out_cubic,
    easeInQuart as ease_in_quart,
    easeOutQuart as ease_out_quart,
    easeInOutQuart as ease_in_out_quart,
    easeInQuint as ease_in_quint,
    easeOutQuint as ease_out_quint,
    easeInOutQuint as ease_in_out_quint,
    easeInSine as ease_in_sine,
    easeOutSine as ease_out_sine,
    easeInOutSine as ease_in_out_sine,
    easeInExpo as ease_in_expo,
    easeOutExpo as ease_out_expo,
    easeInOutExpo as ease_in_out_expo,
    easeInCirc as ease_in_circ,
    easeOutCirc as ease_out_circ,
    easeInOutCirc as ease_in_out_circ,
    easeInElastic as ease_in_elastic,
    easeOutElastic as ease_out_elastic,
    easeInOutElastic as ease_in_out_elastic,
    easeInBack as ease_in_back,
    easeOutBack as ease_out_back,
    easeInOutBack as ease_in_out_back,
    easeInBounce as ease_in_bounce,
    easeOutBounce as ease_out_bounce,
    easeInOutBounce as ease_in_out_bounce,
)
