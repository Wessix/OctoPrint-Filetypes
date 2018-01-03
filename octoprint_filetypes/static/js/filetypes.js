/*
 * View model for OctoPrint-Filetypes
 *
 * Author: thelongrunsmoke
 * License: AGPLv3
 */
$(function() {
    function FiletypesViewModel(parameters) {
        var self = this;
	    self.settings = parameters[0];

	    self.type = {
	        stl : ko.observable(),
	        gcode : ko.observable(),
	        gco : ko.observable(),
	        g : ko.observable(),
            hextemp : ko.observable()
	    };

	    self.updateTypes = function(){
	        var keys = Object.keys(self.type);
	        var result = [];
	        keys.forEach(function(key){
	            if (self.type[key]()) result.push("."+key);
	        });
	        $('#gcode_upload').attr('accept', result.join(','));
	    };

        self.onBeforeBinding = function() {
            var keys = Object.keys(self.type);
            // Initialize each element in model
            keys.forEach(function(key) {
                self.type[key](self.settings.settings.plugins.filetypes[key]());
            });
            // Bind subscriber to views.
            keys.forEach(function(key) {
                self.type[key].subscribe(self.updateTypes);
            });
		    self.updateTypes();
        }
    }

    OCTOPRINT_VIEWMODELS.push([
        FiletypesViewModel,
        [ "settingsViewModel"],
        [ "#settings_plugin_filetypes" ]
    ]);
});
