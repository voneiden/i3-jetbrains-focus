# i3 Jetbrains Focus

Automatic focus_follows_mouse setter to keep jetbrains dialogs from closing accidentally using IPC in i3 and Sway.

It's rather quite simple: When focus lands on a jetbrains dialog, focus_follows_mouse is set to no. When focus lands
anywhere else, focus_follows_mouse is set to either yes/always depending on configuration.

## Configuration via environment variables

JETBRAINS_FOCUS_DEFAULT_MODE allows determining the default mode for focus and it defaults to "yes". In Sway it is
also possible to use "always".


