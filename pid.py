import numpy as np

import matplotlib.pyplot as plt


class pid:
    def __init__(self, KP, KI, KD):
        self.KP = KP
        self.KI = KI
        self.KD = KD
        self.error = 0
        self.integral_error = 0
        self.error_prev = 0
        self.derivative_error = 0

    def get_output(self, pos, target, dt):
        self.error = target - pos
        self.integral_error += self.error * dt
        self.derivative_error = (self.error - self.error_prev) / dt
        self.error_prev = self.error
        self.output = (
            self.KP * self.error
            + self.KI * self.integral_error
            + self.KD * self.derivative_error
        )

        return self.output


if __name__ == "__main__":
    KP = 0.45
    KI = 10
    KD = 0.0
    y_0 = 0
    t_start = 0
    t_end = 1
    dt = 0.005
    target_y = 15

    controller = pid(KP, KI, KD)

    y = np.array([y_0])
    t = np.arange(t_start, t_end + dt, dt)

    for i in range(len(t) - 1):
        dy = controller.get_output(y[i], target_y, dt)
        y = np.append(y, y[i] + dy)

    plt.plot(t, y)
    plt.plot(t, [target_y] * len(t), "--")
    plt.show()
