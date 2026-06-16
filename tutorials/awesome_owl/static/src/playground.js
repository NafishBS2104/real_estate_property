/** @odoo-module **/
import {Component, markup, useState} from "@odoo/owl";

import {Counter} from "./components/Counter/counter";
import {Card} from "./components/Card/card";
import {Todo} from "./components/Todo/todo_list";

export class Playground extends Component {
    static template = "awesome_owl.playground";
    static components = {Counter, Card,Todo}

    setup() {
        this.state = useState({
            sum: 2
        });
        this.htmlContent = markup("<div class='text-primary'>content</div>");
        this.normalContent = "<div class='text-primary'>content</div>";
    }
    incrementSum() {
        this.state.sum++;
    }
}