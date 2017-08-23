# How to add file extension

1. In [`__init__.py`](https://github.com/TheLongRunSmoke/OctoPrint-Filetypes/blob/master/octoprint_filetypes/static/js/filetypes.js), add your extension in to dictionary in get_settings_defaults(), and make according fix in get_template_vars().

2. In [filetypes.js](https://github.com/TheLongRunSmoke/OctoPrint-Filetypes/blob/master/octoprint_filetypes/static/js/filetypes.js), add extension to self.type.

3. In [filetypes_settings.jinja2](https://github.com/TheLongRunSmoke/OctoPrint-Filetypes/blob/master/octoprint_filetypes/templates/filetypes_settings.jinja2), add control for your extension.

# YAML configuration

You can specify plugin configuration in octoprint's `config.yaml`. In `plugins` section, for example:

```
filetypes:
    g: false
    gco: false
    slt: false
```