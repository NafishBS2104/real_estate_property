import {Component,useState,onWillStart} from "@odoo/owl";
import {registry} from "@web/core/registry";
import {useService} from "@web/core/utils/hooks";
import {EmployeeCard} from "../components/employee_card/employee_card";

export class AttendanceDashboard extends Component{

    static template = "attendance_dashboard.AttendanceDashboard";
    static components = {
        EmployeeCard,
    };

    setup(){
        this.orm = useService("orm");
        this.state = useState({
            search: "",
            employees:[],
            loading: true,
            error: false,
        });

        onWillStart(async () => {
            await this.loadAttendance();
        });
    }

    async loadAttendance(){
        try{
            const records = await this.orm.searchRead(
                "hr.attendance",
                [],
                [
                    "employee_id",
                    "check_in",
                    "check_out",
                    "worked_hours",
                ]
            );

            this.state.employees = records.map((record) => ({
                id: record.id,
                name: record.employee_id ? record.employee_id[1] : "Unknown",
                check_in: record.check_in || "-",
                check_out: record.check_out || "-",
                hours: record.worked_hours || 0,
            }));
        } catch (error){
            console.error("failed to load attendance:",error);
            this.state.error = true;
        } finally{
            this.state.loading = false;
        }
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