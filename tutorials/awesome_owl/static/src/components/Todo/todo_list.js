/** @odoo-module **/
import {useState,Component,xml} from "@odoo/owl";
import {TodoItem} from "./todo_item";


export class Todo extends Component{
    static template = xml`
        <div class="todo-list">
            <!-- New input field -->
            <input
               type="text"
               placeholder="Enter a new task"
               t-on-keyup="addTodo"/>

                <!-- Existing todo list -->
                <t t-foreach="this.todos" t-as="todo" t-key="todo.id">
                  <TodoItem todo="todo"/>
                </t>
           </div>
    `;

    static components = {
        TodoItem,
    };

    setup(){
        this.todos = useState([]);
        this.nextId = 1;
    }

    addTodo(ev){
        if(ev.keyCode !== 13){
            return;
        }
        const input = ev.target;
        const description = input.value.trim();

        this.todos.push(
            {
                id: this.nextId++,
                description: description,
                isComplete: false,
            }
        );
        this.value = "";
    }
}
