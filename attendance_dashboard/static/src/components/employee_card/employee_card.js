import {Component} from "@odoo/owl";

export class EmployeeCard extends Component{
    static template = "attendance_dashboard.EmployeeCard";

    static props = {
        employee: Object,
    };

    get attendanceStatus(){
        const hours = this.props.employee.hours;

        if(hours >= 9)
        {
            return "Present";
        }
        if(hours >= 8)
        {
            return "Half Day";
        }
        return "Absent";
    }

    get statusClass(){
        const hours = this.props.employee.hours;

        if(hours >= 9)
        {
            return "text-success";;
        }
        if(hours >= 8)
        {
            return "text-primary";
        }
        return "text-danger";
    }

    get hoursClass(){
        const hours = this.props.employee.hours;

        if(hours >= 9)
        {
            return "hours-green";;
        }
        if(hours >= 8)
        {
            return "hours-blue";
        }
        return "hours-red";
    }
}