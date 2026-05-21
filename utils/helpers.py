import math
import numpy as np


def calculate_distance(point1, point2):
    """
    Calculate distance between two points.
    """

    x1, y1 = point1
    x2, y2 = point2

    distance = math.hypot(x2 - x1, y2 - y1)

    return distance


def map_volume(distance,
               min_distance=30,
               max_distance=250,
               min_volume=0,
               max_volume=100):
    """
    Convert hand distance into volume percentage.
    """

    volume = np.interp(
        distance,
        [min_distance, max_distance],
        [min_volume, max_volume]
    )

    return int(volume)


def clamp(value, min_value, max_value):
    """
    Restrict value within range.
    """

    return max(min_value, min(value, max_value))


def smooth_value(previous_value,
                 current_value,
                 smoothing_factor=5):
    """
    Smooth sudden value changes.
    """

    smoothed = previous_value + (
        current_value - previous_value
    ) / smoothing_factor

    return smoothed