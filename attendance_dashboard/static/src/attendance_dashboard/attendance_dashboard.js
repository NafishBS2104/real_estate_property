import {Component,useState} from "@odoo/owl";
import {registry} from "@web/core/registry";

export class AttendanceDashboard extends Component{

    static template = "attendance_dashboard.AttendanceDashboard";

    setup(){
        this.state = useState({
            search: "",
            employees:[
              {
                    id: 1,
                    name: "John Doe",
                    check_in: "2026-06-08 09:00:00",
                    check_out: "2026-06-08 18:00:00",
                    hours: 9
                },
                {
                    id: 2,
                    name: "Alice",
                    check_in: "2026-06-08 08:30:00",
                    check_out: "2026-06-08 17:30:00",
                    hours: 9
                }
            ]
        });
    }

    get filteredEmployees(){
        const search = this.state.search.toLowerCase().trim();

        if(!search){
            return this.state.employees;
        }

        return this.state.employees.filter((employee) => employee.name.toLowerCase().includes(search));
    }

    get totalEmployees(){
        return this.filteredEmployees.length;
    }

    get totalEmployees(){
        return this.filteredEmployees.length;
    }

    get totalEmployee(){
        return this.filteredEmployees.length;
    }
    get totalHours(){
        return this.filteredEmployees.reduce(
        (sum,employee) => sum + employee.hours,
         0
        );
    }

    get averageHours(){
        if(this.totalEmployees === 0)
         {
            return 0;
         }
        return (this.totalHours / this.totalEmployees).toFixed(2);
    }

    getHoursClass(hours){
        if(hours >= 9){
            return "hours-green";
        }
        if(hours >= 8){
            return "hours-blue";
        }
        return "hours-red";
    }
}

registry.category("actions").add("attendance_dashboard",AttendanceDashboard);