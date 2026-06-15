/** @odoo-module **/
import { Component,useState } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { Counter } from "./components/Counter/counter";
import {Card} from "./components/Card/card";

export class Playground extends Component {
    static template = "awesome_owl.playground";
    static components = { Counter, Card};
}
registry.category("actions").add("awesome_owl.playground",Playground)