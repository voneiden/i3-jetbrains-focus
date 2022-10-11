import os

from i3ipc import Connection, Event

disabled = False


def main():
    i3 = Connection()

    # Sway also supports "always"
    default_mode = os.getenv('JETBRAINS_FOCUS_DEFAULT_MODE', 'yes')

    def on_window_focus(i3, e):
        global disabled

        focused = i3.get_tree().find_focused()

        if focused.window_class and focused.window_class.startswith('jetbrains') and focused.type == 'floating_con':
            if not disabled:
                i3.command('focus_follows_mouse no')
                disabled = True
        elif disabled:
            i3.command(f'focus_follows_mouse {default_mode}')
            disabled = False

    i3.on(Event.WINDOW_FOCUS, on_window_focus)
    i3.main()


if __name__ == '__main__':
    main()
