# The use of the NVIDIA bindings is enabled by setting the environment variable NUMBA_CUDA_USE_NVIDIA_BINDING to "1".
# sysdm.cpl

from numba import njit
from numba import jit
import random
import numpy as np
import os
os.environ["NUMBA_CUDA_USE_NVIDIA_BINDING"] = "1"

@njit(nogil=True, cache=True)  # nogil=True, parallel=True cache=True
def monte_carlo_pi(nsamples):
    acc = 0
    for i in range(nsamples):
        x = random.random()
        y = random.random()
        if (x ** 2 + y ** 2) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples

@jit(nopython=True)
def zero_clamp(x, threshold):
    out = np.empty_like(x)
    for i in range(out.shape[0]):
        if np.abs(x[i]) > threshold:
            out[i] = x[i]
        else:
            out[i] = 0
    return out  

x = monte_carlo_pi(1000000000)
print(x)
a_small = np.linspace(0, 1, 500)
r = zero_clamp(a_small, 0.3)
print(r)