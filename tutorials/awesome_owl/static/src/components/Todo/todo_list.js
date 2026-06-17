/** @odoo-module **/
import {Component, useState, useRef, onMounted, xml} from "@odoo/owl";
import {TodoItem} from "./todo_item";


export class Todo extends Component{
   static template = "awesome_owl.TodoList";

    static components = {
        TodoItem,
    };

    setup(){
        this.todos = useState([
            {
                id: 1,
                description: "Writing Code",
                isCompleted: true,
            },
            {
                id: 2,
                description: "Reading Document",
                isCompleted: false,
            },
        ]);
        this.nextId = 3;
    }

    toggleState(id){
        const todo= this.todos.find(todo => todo.id === id);
        if(todo){
           todo.isCompleted = !todo.isCompleted;
        }
         }
    addTodo(ev){
        if(ev.keyCode !== 13){
            return;
        }
        const input = ev.target;
        const description = input.value.trim();
        if(!description){
            return;
        }

        this.todos.push(
            {
                id: this.nextId++,
                description: description,
                isCompleted: false,
            }
        );
        input.value = "";
    }

        removeTodo(id){
              const index = this.todos.findIndex(todo => todo.id === id);
              if(index >= 0){
                  this.todos.splice(index,1);
              }
        }
    }