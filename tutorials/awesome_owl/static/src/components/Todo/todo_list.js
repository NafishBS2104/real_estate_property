/** @odoo-module **/
import {useState,Component} from "@odoo/owl";
import {TodoItem} from "./todo_item";


export class Todo extends Component{
    static template = "awesome_owl.TodoList";

    static components = {
        TodoItem,
    };

    setup(){
        this.todos = useState([
            {
                id: 3,
                description: "buy milk",
                isCompleted: false,
            },
            {
              id: 2,
              description: "Write Tutorials",
              isCompleted: true,
            },
        ]);
    }
}
