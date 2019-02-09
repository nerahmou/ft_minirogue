# coding utf8
# lang: python3


def welcome(window):
    msg = [ "Welcome to ft_minirogue",
    "ft_minirogue: Adventure Game",
    "By: nerahmou and timfuzea"]
    i = 2
    for string in msg:
        tmp_y = int(50 - int(len(string) / 2))
        window.addstr(i, tmp_y, string)
        i = i + 2
    window.refresh()
