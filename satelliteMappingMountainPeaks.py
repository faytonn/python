import sys


def find_peaks():
    prev = None
    current = None
    plateau_start = None
    plateau_height = None
    pos = 0

    for line in sys.stdin:
        elevation_str = line.strip()
        try:
            elevation = float(elevation_str)
        except ValueError:
            continue

        if elevation < 0:
            break

        if current is not None:
            if prev is not None:
                if current > prev and current > elevation:
                    print(f"distance {pos - 1} height {round(current, 1):.1f}")
                elif current == elevation and (plateau_start is None):
                    plateau_start = pos - 1
                    plateau_height = current
                elif current != elevation and plateau_start is not None:
                    if plateau_height > prev and plateau_height > elevation:
                        print(
                            f"distance {plateau_start} height {round(plateau_height, 1):.1f}"
                        )
                    plateau_start = None
                    plateau_height = None

            prev = current
            current = elevation
            pos += 1
        else:
            current = elevation
            pos += 1


find_peaks()