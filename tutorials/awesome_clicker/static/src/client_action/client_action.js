/** @odoo-module **/
import {Component,useState} from "@odoo/owl";
import {useService} from "@web/core/utils/hooks";
import {registry} from "@web/core/registry";


export class ClickerClientAction extends Component{
    static template = "awesome_clicker.ClickerClientAction";
    static props = ["*"];

    setup(){
        this.clickService = useState(useService("awesome_clicker.clicker"));
    }
}

registry.category("actions").add("awesome_clicker.client_action",ClickerClientAction);