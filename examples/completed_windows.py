"""Educational time-boundary example; no strategy or financial observations.

Indexes refer to an existing chronological sequence. The sample demonstrates
excluding entries whose forward outcomes are still incomplete at a cutoff.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class CompletedWindow:
    start: int
    cutoff: int
    eligible_entries: tuple[int, ...]


def completed_windows(bar_count: int, window_bars: int, step_bars: int,
                      horizon: int) -> tuple[CompletedWindow, ...]:
    """Return rolling windows and entry indexes with exits inside each window."""
    for value in (bar_count, window_bars, step_bars, horizon):
        if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
            raise ValueError("Counts must be positive integers")
    if window_bars > bar_count or horizon >= window_bars:
        raise ValueError("A window must fit the history and contain a completed outcome")
    ends = list(range(window_bars, bar_count + 1, step_bars))
    if ends[-1] != bar_count:
        ends.append(bar_count)
    return tuple(
        CompletedWindow(end - window_bars, end - 1,
                        tuple(range(end - window_bars, end - horizon)))
        for end in ends
    )


if __name__ == "__main__":
    for window in completed_windows(12, window_bars=6, step_bars=4, horizon=2):
        print(f"Window {window.start}..{window.cutoff}; "
              f"completed entry indexes: {window.eligible_entries}")
