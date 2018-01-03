# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin


class FiletypesPlugin(octoprint.plugin.StartupPlugin,
					  octoprint.plugin.TemplatePlugin,
					  octoprint.plugin.SettingsPlugin,
					  octoprint.plugin.AssetPlugin):

	def get_template_configs(self):
		return [
			dict(type="settings")
		]

	def on_after_startup(self):
		self._logger.info("Filetypes. (settings: stl=%s, gcode=%s, gco=%s, g=%s, hextemp=%s)" % (self._settings.get(["stl"]), self._settings.get(["gcode"]), self._settings.get(["gco"]), self._settings.get(["g"]), self._settings.get(["hextemp"])))

	##~~ SettingsPlugin mixin
	def get_settings_defaults(self):
		"""
		Return defaults.
		:return: dict  
		"""
		return dict(
			stl=True,
			gcode=True,
			gco=True,
			g=True,
			hextemp=True
		)

	def get_template_vars(self):
		return dict(
			stl=self._settings.get(["stl"]),
			gcode=self._settings.get(["gcode"]),
			gco=self._settings.get(["gco"]),
			g=self._settings.get(["g"]),
			hextemp=self._settings.get(["hextemp"])
		)

	##~~ AssetPlugin mixin
	def get_assets(self):
		# Define your plugin's asset files to automatically include in the
		# core UI here.
		return dict(
			js=["js/filetypes.js"]
		)

	##~~ Softwareupdate hook
	def get_update_information(self):
		# Define the configuration for your plugin to use with the Software Update
		# Plugin here. See https://github.com/foosel/OctoPrint/wiki/Plugin:-Software-Update
		# for details.
		return dict(
			filetypes=dict(
				displayName="Filetypes Plugin",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="TheLongRunSmoke modified by Wessix",
				repo="OctoPrint-Filetypes",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/TheLongRunSmoke/OctoPrint-Filetypes/archive/{target_version}.zip"
			)
		)


__plugin_name__ = "Filetypes Plugin"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = FiletypesPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}
