<template>
    <div class="calendar">
        <div class="calendar-header">
            <a @click="changeMonth(-1)"><img src="/arrow.png" style="transform: rotate(90deg);"></a>
            <label class="text-small bold">{{monthNames[Math.abs(show_month) % monthNames.length]}} {{show_month_first_date.getFullYear()}}</label>
            <a @click="changeMonth(1)"><img src="/arrow.png" style="transform: rotate(-90deg);"></a>
        </div>

        <!-- Календарь - Числа -->
        <div class="calendar_table_days" id="calendar_table_days">
            <label v-for="day in weekdaysNames">{{day}}</label>
            <button v-for="day in days" class="btn text"
            @click="selectDate(day)"
            :class="{
                'bold': (dayIsEquels(day, currentDate) == true),
                'bg-gray': dayAllowedColor(day),
                'selected': selected_days[day] != undefined}"
            >
                {{day.getDate()}}
            </button>
        </div>

    </div>
</template>

<script setup lang="ts">
import {ref} from 'vue'

const monthNames = [
    'январь',
    'февраль',
    'март',
    'апрель',
    'май',
    'июнь',
    'июль',
    'август',
    'сентябрь',
    'октябрь',
    'ноябрь',
    'декабрь'
]

const weekdaysNames = ["пн", "вт", "ср", "чт", "пт", "сб", "вс"]

const props = defineProps({
    multiple: {type: Boolean, required: false, default: false},
    sessions: {type: Array<any>, required: false, default: []},
    allow_today: {type: Boolean, required: false, default: false}
})

let currentDate = new Date()
currentDate = new Date(currentDate.getFullYear(), currentDate.getMonth(), currentDate.getDate())

let days = ref([])
let selected_days = ref({})

let show_month = ref(currentDate.getMonth())
let show_month_first_date = ref(null);
let show_month_last_date = ref(null);

function dayIsEquels(the_day, other_day) {
    let res =  other_day.getDate()==the_day.getDate() && other_day.getMonth() == the_day.getMonth() && other_day.getFullYear() == the_day.getFullYear()
    return res
    
}

function day_in_session(day) {
    for (const session in props.sessions) {
        if (dayIsEquels(day, new Date(session.date))){
            return true
        }
    }
    
    return false
}

function day_allowed(day) {
    if (props.sessions.length > 0){
        return day_in_session(day)
    }

    if (props.allow_today)
        return day >= currentDate
    else
        return day > currentDate
}

function dayAllowedColor(day){
    
    // return ((day < show_month_first_date && day <= show_month_last_date) || (day > show_month_last_date))
    return day_allowed(day)
}

async function selectDate(day) {

    // Запрет на запись на дни раньше или текущий
    if (!day_allowed(day)){
        return
    }

    
    if (selected_days.value[day] == undefined){
        if (!props.multiple){
            selected_days.value = {}
        }

        selected_days.value[day] = true
    }else{
        delete selected_days.value[day]
    }

    
    console.log(selected_days.value)
   
}

async function changeMonth(from_current: number){
    let next_month = show_month.value + from_current
    show_month.value = next_month
    days.value = await generateCalendar(currentDate.getFullYear(), next_month)
    show_month_first_date.value = new Date(currentDate.getFullYear(), show_month.value, 1);
    show_month_last_date.value = new Date(currentDate.getFullYear(), show_month.value+1, 0);

}



async function generateCalendar(currentYear:number, monthNumber:number) {
  // Get the first day of the month
  let firstDayOfMonth = new Date(currentYear, monthNumber, 1);

  // Find the closest Monday before or on the first day of the month
  let firstMonday = new Date(firstDayOfMonth);
  firstMonday.setDate(firstMonday.getDate() - (firstMonday.getDay() + 6) % 7);

  // Find the closest Sunday after or on the last day of the month
  let lastDayOfMonth = new Date(currentYear, monthNumber+1, 0);
  let lastSunday = new Date(lastDayOfMonth);
  lastSunday.setDate(lastSunday.getDate() + (7 - lastSunday.getDay()) % 7);

  // Generate the calendar dates
  let calendar = [];
  let date = new Date(firstMonday);

  // Generate six weeks of dates
  for (let i = 0; i < 6 * 7; i++) {
    calendar.push(new Date(date));
    date.setDate(date.getDate() + 1);
  }

  return calendar;
}

await changeMonth(0)


</script>


<style scoped>

.calendar_table_weekday{
    display: grid;
    align-items: center;
    text-align: center;
    grid-template-columns: repeat(7, calc(100%/7));
    margin-bottom: 20px;
}

.calendar_table_days{
    display: grid;
    align-items: center;
    text-align: center;
    justify-content: center;
    gap: 5px;
    grid-template-columns: repeat(7, calc(100%/7));
    height: calc(48px * 7);
    padding: 10px;
}

.calendar_table_days > button{
    height: 100%;
    background-color: transparent;
    border: 0;
}

.calendar_table_days .circler {
    
    margin: auto;
    aspect-ratio: 1/1;
    border-radius: 50%
}


.calendar-header{
    display: flex;
    justify-content: space-between;
    padding: 25px;
}

.current{
    background-color: var(--primary-light-color) !important;
    font-weight: 600;
}


.selected{
    background-color: var(--primary-color) !important;
}

.calendar{
    width: 100%;
}

</style>