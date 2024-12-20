import time
import os
import sys


def time_format(duration):
    """
    Formats the duration time in the most common format of the original
    tqdm function.
    """
    if duration < 1:
        return "00:00"
    elif duration < 3600:
        minutes, seconds = divmod(int(duration), 60)
        return f"{minutes:02}:{seconds:02}"
    else:
        hours, remainder = divmod(int(duration), 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours}:{minutes:02}:{seconds:02}"


def ratio_done(idx, total):
    """
    Returns a string with the ratio of completed iterations over the total.
    """
    return f'{str(idx)}/{str(total)}'


def time_spent(elap_time):
    """
    Returns the elapsed time in a proper format.
    """
    return time_format(elap_time)


def time_left(idx, total, elap_time):
    """
    Calculates the remaining time based on the iterations
    already completed and the elapsed time up to the current
    moment, and returns it in a proper format.
    """
    if idx == 0:
        return '?'
    else:
        return time_format(elap_time * (total / idx) - elap_time)


def speed_for_it(idx, elap_time):
    """
    Calculates the average speed of the process, measured in
    iterations per second(it/s). Note that the original tqdm
    function may sometimes measure in seconds per iteration (s/it).
    """
    if idx == 0:
        return '?it/s'
    elif elap_time == 0:
        return '?it/s'
    else:
        return f'{idx / elap_time:.2f}it/s'


def info_bar(idx, total, elap_time):
    """
    Returns a string containing the process information, aiming
    to emulate the format of the original tqdm function.
    """
    ratio = ratio_done(idx, total)
    time_now = time_spent(elap_time)
    time_to_fin = time_left(idx, total, elap_time)
    speed = speed_for_it(idx, elap_time)
    return f'{ratio} [{time_now}<{time_to_fin}, {speed}]'


def percentage(ratio_complete):
    """
    Returns a string with the percentage of the process completed.
    """
    return f'{(ratio_complete) * 100:.0f}%'


def print_info_by_idx(idx, total, start_time):
    """
    Calculate the length of the strings corresponding to the percentage,
    the information bar, the progress bar length, and the represented
    progress, then display them on the screen.
    """
    ratio_complete = idx / total
    percent = percentage(ratio_complete)
    elap_time = time.time() - start_time
    inf_bar = info_bar(idx, total, elap_time)
    bar_length = (os.get_terminal_size().columns
                  - len(percent) - len(inf_bar) - 3)
    fill_char = '█' * int(ratio_complete * bar_length)
    spaces = ' ' * (bar_length - len(fill_char))
    sys.stdout.write(f'\r{percent}|{fill_char}{spaces}| {inf_bar}')
    sys.stdout.flush()


def ft_tqdm(lst: range) -> None:
    """
    Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested.
    """
    total = len(lst)
    start_time = time.time()
    for idx, elem in enumerate(lst):
        print_info_by_idx(idx, total, start_time)
        yield elem
    print_info_by_idx(idx + 1, total, start_time)
    print()
    return None

