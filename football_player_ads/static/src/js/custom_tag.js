
/** @odoo-module **/
import { registry } from "@web/core/registry";
import { Component } from "@odoo/owl"

class CustomAction extends Component {}
CustomAction.template = "CustomActions" // this is reported to the xml folder

registry.category("actions").add("custom_client_action", CustomAction);




// Same stuff as above, different syntax according to different odoo versions
//odoo.define('football_player_ads.CustomAction', function(require) {
//  "use strict";

//  var AbstractActionrequire('web.AbstractAction');
//  var core = require('web.core');

//  AbstractAction.extend({
//    template: "CustomActions";
//    start: function() {
//      console.log("Action")
//    }
//  })

//  core.action_registry.add("custom_client_action", CustomAction)
//});
