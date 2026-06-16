/** @odoo-module **/
import { Component,markup } from "@odoo/owl";

import { Counter } from "./components/Counter/counter";
import {Card} from "./components/Card/card";

export class Playground extends Component {
    static template = "awesome_owl.playground";
    static components = { Counter, Card}
    setup(){
        this.htmlContent = markup("<div class='text-primary'>content</div>");
        this.normalContent = "<div class='text-primary'>content</div>";
    }
}
